# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-23 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20171223_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='genre',
            field=models.CharField(blank=True, choices=[('C', 'Corbalar'), ('Y', 'Yemek'), ('A', 'Atıştırmalık'), ('S', 'Salata'), ('T', 'Tatlı')], max_length=80),
        ),
    ]