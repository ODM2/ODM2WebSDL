# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-14 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataloaderinterface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydrosharesitesetting',
            name='update_freq',
            field=models.IntegerField(null=True),
        ),
    ]
