# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('dash_docs_app', '0005_auto_20180928_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentedmodel',
            name='holder_plugin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='holder_plugin', to='cms.CMSPlugin'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documentedmodel',
            name='parent_plugin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_plugin', to='cms.CMSPlugin'),
        ),
    ]
