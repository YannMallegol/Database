# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='age_patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(default=0)),
                ('identity', models.ForeignKey(to='version_1.Identity')),
            ],
        ),
    ]
