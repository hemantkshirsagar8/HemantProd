# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-21 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneer', '0017_auto_20170421_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='wing',
            field=models.CharField(max_length=5),
        ),
    ]