# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-25 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_auto_20170125_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='proposal',
        ),
    ]