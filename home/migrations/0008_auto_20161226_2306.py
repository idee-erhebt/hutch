# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-26 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_registrated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrated',
            name='ideaName',
            field=models.CharField(default=b'aa', max_length=20),
        ),
    ]
