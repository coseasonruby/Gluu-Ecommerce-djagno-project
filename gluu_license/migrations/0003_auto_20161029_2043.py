# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluu_license', '0002_auto_20161029_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='public_key',
            field=models.CharField(max_length=250),
        ),
    ]
