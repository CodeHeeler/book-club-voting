# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_election_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='close',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
