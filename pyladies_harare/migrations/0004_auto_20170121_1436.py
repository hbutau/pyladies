# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pyladies_harare', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='fromdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='From date'),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='todate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='To date'),
        ),
    ]