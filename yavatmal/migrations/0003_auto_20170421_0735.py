# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-21 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yavatmal', '0002_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
