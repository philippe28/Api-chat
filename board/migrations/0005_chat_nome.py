# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20151012_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='nome',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
