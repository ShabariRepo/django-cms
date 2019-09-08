from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core.fields import StreamField
from wagtail.search import index

from streams import blocks


class KbIndexPage(Page):
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        kbpages = self.get_children().live().order_by('-first_published_at')
        context['kbpages'] = kbpages
        return context

class KbPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    # body = RichTextField(blank=True)

    # stream field for multiple body elements
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
        ],
        null=True,
        blank=True,
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('documents', label="Documents"),
        # FieldPanel('body', classname="full"),
        StreamFieldPanel("content"),
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

    