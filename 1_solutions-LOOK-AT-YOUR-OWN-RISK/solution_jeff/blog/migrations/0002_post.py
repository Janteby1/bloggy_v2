# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=4000)),
                ('slug', models.SlugField(max_length=40)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, default=None, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_DEFAULT)),
            ],
        ),
    ]
