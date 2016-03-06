# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20160211_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slugs',
        ),
    ]
