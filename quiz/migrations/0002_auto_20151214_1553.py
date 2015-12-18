# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Content', 'verbose_name_plural': 'Content items'},
        ),
        migrations.AlterModelOptions(
            name='useranswer',
            options={'verbose_name': 'User answer', 'verbose_name_plural': 'User answers'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='ordinal',
        ),
    ]
