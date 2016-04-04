# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20160404_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('U', 'Inconnu')], default=1, max_length=1),
        ),
    ]