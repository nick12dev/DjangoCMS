# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_addon', '0003_auto_20180925_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsaveposition',
            name='is_resized',
            field=models.CharField(max_length=50, null=True),
        ),
    ]