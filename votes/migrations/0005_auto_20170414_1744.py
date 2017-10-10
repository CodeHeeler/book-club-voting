# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170414_1722'),
        ('votes', '0004_auto_20170414_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ballot',
            old_name='choices',
            new_name='selections',
        ),
        migrations.AddField(
            model_name='election',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='election_won', to='books.Book'),
        ),
    ]
