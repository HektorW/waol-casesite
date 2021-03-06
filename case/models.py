from django.db import models

# Create your models here.

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class CasePage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]
