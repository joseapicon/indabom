# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-15 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0012_auto_20170415_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpart',
            name='ncnr',
            field=models.BooleanField(default=False),
        ),
    ]