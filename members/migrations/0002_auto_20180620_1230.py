# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pics',
            field=models.ImageField(default=b'media/background.jpg', upload_to=b''),
        ),
    ]
