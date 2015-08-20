# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MRN_DBID_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='type_of_analyse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DIFFUSION', models.CharField(max_length=20)),
                ('Localizer', models.CharField(max_length=20)),
                ('MPRAGE', models.CharField(max_length=20)),
                ('identity', models.ManyToManyField(to='version_1.Identity')),
            ],
        ),
    ]
