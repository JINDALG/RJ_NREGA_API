# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170320_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='districy_id',
            new_name='district_id',
        ),
    ]
