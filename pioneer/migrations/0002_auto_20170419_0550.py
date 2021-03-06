# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-19 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pioneer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('society', models.CharField(max_length=200)),
                ('phase', models.IntegerField(max_length=50)),
                ('wing', models.CharField(max_length=50)),
                ('flat_no', models.IntegerField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]
