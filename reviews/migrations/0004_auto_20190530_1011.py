# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-30 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190529_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Profile'),
        ),
    ]
