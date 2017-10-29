# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_auto_20171020_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='bttle',
            new_name='btitle',
        ),
    ]
