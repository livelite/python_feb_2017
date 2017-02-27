# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20170220_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='message_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
