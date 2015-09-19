from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from case.models import CasePage


class HomePage(Page):

    def cases(self):
        return CasePage.objects.live().descendant_of(self)
