# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0004_auto_20171020_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='h1',
            fields=[
                ('hid', models.AutoField(serialize=False, primary_key=True)),
                ('hostname', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='h2',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('h2g', models.ManyToManyField(to='book_app.h1')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('hid', models.AutoField(serialize=False, primary_key=True)),
                ('hostname', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('hgid', models.AutoField(serialize=False, primary_key=True)),
                ('group_id', models.ForeignKey(to='book_app.Group')),
                ('host_id', models.ForeignKey(to='book_app.Host')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='h2g',
            field=models.ManyToManyField(to='book_app.Host', through='book_app.HostGroup'),
        ),
    ]
