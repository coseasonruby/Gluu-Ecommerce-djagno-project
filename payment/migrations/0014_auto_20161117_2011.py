# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_payment_failed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='failed',
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[(b'INIT', b'Initiated'), (b'PAID', b'Paid'), (b'FAIL', b'Failed')], default=b'INIT', max_length=4),
        ),
    ]
