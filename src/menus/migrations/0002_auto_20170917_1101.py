# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-17 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='comtents',
            new_name='contents',
        ),
    ]
