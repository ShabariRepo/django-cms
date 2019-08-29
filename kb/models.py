from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.models import get_document_model
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index


class KbIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        kbpages = self.get_children().live().order_by('-first_published_at')
        context['kbpages'] = kbpages
        return context

class KbPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    # book_file = models.ForeignKey(
    #     get_document_model(),
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('documents', label="Documents"),
        # DocumentChooserPanel('book_file'),
    ]

# image on each blog page from the gallery
class KbPageGalleryImage(Orderable):
    page = ParentalKey(KbPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

# document on each blog page from the doc dir
class KbPageDocument(Orderable):
    page = ParentalKey(KbPage, on_delete=models.CASCADE, related_name='documents')
    doc = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        DocumentChooserPanel('doc'),
        FieldPanel('caption'),
    ]

    