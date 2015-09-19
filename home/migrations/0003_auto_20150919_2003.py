# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading',
            field=models.TextField(default=datetime.datetime(2015, 9, 19, 18, 3, 28, 518874, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
