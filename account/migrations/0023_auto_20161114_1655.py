# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20161114_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='initial_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='credit',
            name='remaining_amount',
            field=models.FloatField(),
        ),
    ]