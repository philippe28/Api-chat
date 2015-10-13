# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_chat_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='slug',
            field=models.SlugField(verbose_name=django.contrib.auth.models.User),
        ),
    ]
