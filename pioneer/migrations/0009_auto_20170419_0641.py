# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-19 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pioneer', '0008_auto_20170419_0639'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Society',
            new_name='SocietyMember',
        ),
    ]