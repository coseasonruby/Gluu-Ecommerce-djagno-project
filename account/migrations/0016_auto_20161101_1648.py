# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20161101_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit',
            old_name='amount',
            new_name='initial_amount',
        ),
        migrations.AddField(
            model_name='credit',
            name='remaining_amount',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=6),
            preserve_default=False,
        ),
    ]
