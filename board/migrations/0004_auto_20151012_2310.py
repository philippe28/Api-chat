# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20151012_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='nome',
        ),
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
