# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-27 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_chatted'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatted',
            name='ideaId',
            field=models.IntegerField(default=-999999),
        ),
    ]
