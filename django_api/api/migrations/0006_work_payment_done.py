# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170320_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='payment_done',
            field=models.BooleanField(default=False),
        ),
    ]
