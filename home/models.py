from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


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

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel("banner_title"),
    ]

class Meta:

    verbose_name = "Centrilogic CMS - Home Page"
    verbose_name_plural = "Centrilogic CMS - Home Pages"