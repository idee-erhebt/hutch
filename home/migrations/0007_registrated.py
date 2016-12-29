# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-20 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_addques'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], max_length=1, verbose_name=b'Gender      ')),
                ('phoneNumber', models.CharField(blank=True, max_length=10)),
                ('mailId', models.EmailField(max_length=50)),
                ('ideaid', models.IntegerField(default=0)),
                ('ideaName', models.CharField(max_length=20)),
            ],
        ),
    ]