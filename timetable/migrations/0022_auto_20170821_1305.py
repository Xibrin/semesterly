# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-21 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0021_auto_20170820_1323"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="level",
            field=models.CharField(default=b"", max_length=500, null=True),
        ),
    ]
