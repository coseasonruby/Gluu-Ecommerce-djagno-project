# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20161027_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecommerceuser',
            name='company',
        ),
    ]