# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-21 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneer', '0016_auto_20170421_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phase',
            field=models.CharField(choices=[('one', 'I'), ('two', 'II')], max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='wing',
            field=models.CharField(max_length=10),
        ),
    ]
