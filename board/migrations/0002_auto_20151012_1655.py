# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sprint',
            new_name='Chat',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned',
        ),
        migrations.RemoveField(
            model_name='task',
            name='sprint',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='end',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='description',
            new_name='mensagem',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='name',
            new_name='nome',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
