# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-24 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contest_data',
            fields=[
                ('title', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=15000)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_data')),
            ],
        ),
        migrations.CreateModel(
            name='contest_result_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=100000)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.contest_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_data')),
            ],
        ),
        migrations.CreateModel(
            name='leaderboard_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=100000)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.contest_data')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_data')),
            ],
        ),
    ]
