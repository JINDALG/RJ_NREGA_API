# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-21 02:26
from __future__ import unicode_literals

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AlterModelOptions(
            name='grampanchayat',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AddField(
            model_name='district',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 21, 2, 25, 25, 980456, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2017, 3, 21, 2, 25, 46, 199751, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grampanchayat',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 21, 2, 25, 57, 410067, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grampanchayat',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2017, 3, 21, 2, 26, 2, 891722, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 21, 2, 26, 8, 422941, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2017, 3, 21, 2, 26, 20, 704319, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2017, 3, 21, 2, 26, 27, 195942, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2017, 3, 21, 2, 26, 33, 760594, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
    ]