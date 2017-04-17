# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='patients',
            unique_together=set([('date', 'patient_id')]),
        ),
    ]
