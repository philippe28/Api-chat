# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0005_chat_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='nome',
        ),
        migrations.AddField(
            model_name='chat',
            name='usuario',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
