# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170320_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', related_query_name='work', to='api.Profile'),
        ),
    ]
