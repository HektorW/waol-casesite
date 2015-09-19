from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from case.models import CasePage


class HomePage(Page):
    
    heading = models.TextField()
    description = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('description')
    ]

    def cases(self):
        return CasePage.objects.live().descendant_of(self)
