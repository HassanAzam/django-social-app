# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
    ]
