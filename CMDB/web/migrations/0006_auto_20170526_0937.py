# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170525_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.GroupProfile', verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d'),
        ),
    ]
