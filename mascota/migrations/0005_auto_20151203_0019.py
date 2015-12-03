# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_auto_20151203_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota_perdida',
            name='nombre',
            field=models.CharField(max_length=10),
        ),
    ]
