# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 09:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('choose_distrib', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='container_director',
        ),
        migrations.AddField(
            model_name='container',
            name='container_director',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
