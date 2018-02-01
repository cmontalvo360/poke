# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-30 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke_app', '0003_auto_20180130_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='poke',
            name='pokers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='poke_app.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poke',
            name='users',
            field=models.ManyToManyField(related_name='pokerss', to='poke_app.User'),
        ),
    ]
