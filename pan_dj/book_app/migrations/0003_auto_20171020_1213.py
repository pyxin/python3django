# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_heroinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='yuan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'bing',
            },
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
