# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20151013_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
