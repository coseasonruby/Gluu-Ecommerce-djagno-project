# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20161101_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripecard',
            name='card_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='stripecustomer',
            name='customer_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
