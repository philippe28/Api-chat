# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20151013_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='usuario',
            new_name='nome',
        ),
    ]
