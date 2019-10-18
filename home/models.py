from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


# from wagtail.documents.models import Document, AbstractDocument

# class CustomDocument(AbstractDocument):
#     # Custom field example:
#     source = models.CharField(
#         max_length=255,
#         # This must be set to allow Wagtail to create a document instance
#         # on upload.
#         blank=True,
#         null=True
#     )

#     admin_form_fields = Document.admin_form_fields + (
#         # Add all custom fields names to make them appear in the form:
#         'source',
#     )



class HomePage(Page):
    # body = RichTextField(blank=True)

    # content_panels = Page.content_panels + [
    #     FieldPanel('body', classname="full"),
    # ]
    """Home page model"""
    templates = "home/home_page.html"
    max_count = 1
    body = RichTextField(blank=True)

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+"
    )
    # models.URLField to link to url
    banner_cta = models.ForeignKey(
        "wagtailcore.Page", 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        FieldPanel('body', classname="full")
    ]

class Meta:

    verbose_name = "Centrilogic CMS - Home Page"
    verbose_name_plural = "Centrilogic CMS - Home Pages"