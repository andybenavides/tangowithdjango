# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20160214_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(to='rango.Category', null=True),
        ),
    ]
