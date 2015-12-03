# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0005_auto_20151203_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota_encontrada',
            name='lugar_extravio',
            field=models.ForeignKey(default=0, to='mascota.Mascota_Perdida'),
            preserve_default=False,
        ),
    ]
