# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version_1', '0002_age_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identity',
            old_name='MRN_DBID_text',
            new_name='MRN_DBID',
        ),
    ]
