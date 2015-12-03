# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20151111_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(max_length=20),
        ),
    ]
