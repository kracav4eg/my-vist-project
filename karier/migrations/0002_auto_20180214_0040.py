# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='truckmodel',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]