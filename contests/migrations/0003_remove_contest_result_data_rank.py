# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-24 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_contest_result_data_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest_result_data',
            name='rank',
        ),
    ]