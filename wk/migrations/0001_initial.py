# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WellKnown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=4096)),
                ('value', models.TextField()),
            ],
        ),
    ]
