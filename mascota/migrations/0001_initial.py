# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caza_Recompensas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sexo', models.CharField(max_length=10)),
                ('fecha_nacimiento', models.DateField(verbose_name=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota_Encontrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_encuentro', models.DateField(verbose_name=b'')),
                ('lugar_encuentro', models.CharField(max_length=100)),
                ('id_caza_recompensa', models.ForeignKey(to='mascota.Caza_Recompensas')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota_Perdida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('fecha_extravio', models.DateField(verbose_name=b'')),
                ('lugar_extravio', models.CharField(max_length=100)),
                ('id_mascota', models.ForeignKey(to='mascota.Mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('comuna', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='id_usuario',
            field=models.ForeignKey(to='mascota.Usuario'),
        ),
        migrations.AddField(
            model_name='caza_recompensas',
            name='id_usuario',
            field=models.ForeignKey(to='mascota.Usuario'),
        ),
    ]
