# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20161101_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='account.Account'),
        ),
    ]
