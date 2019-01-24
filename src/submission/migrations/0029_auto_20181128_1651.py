# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 16:51
from __future__ import unicode_literals

from django.db import migrations


def create_missing_configurations(apps, schema_editor):
    Journal = apps.get_model('journal', 'Journal')
    SubmissionConfiguration = apps.get_model('submission', 'SubmissionConfiguration')

    for journal in Journal.objects.all():
        SubmissionConfiguration.objects.get_or_create(journal=journal)


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0028_auto_20181116_1144'),
    ]

    operations = [
        migrations.RunPython(create_missing_configurations, reverse_code=migrations.RunPython.noop),
    ]