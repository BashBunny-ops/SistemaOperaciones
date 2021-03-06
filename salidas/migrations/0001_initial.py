# Generated by Django 2.2.6 on 2020-02-13 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plantas', '0001_initial'),
        ('catalogos', '0001_initial'),
        ('tmuertos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TiempoMuertoEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_produccion', models.DateField()),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('total_tm', models.FloatField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('turno', models.CharField(choices=[('1ER. TURNO', '1ER. TURNO'), ('2DO. TURNO', '2DO. TURNO'), ('3ER. TURNO', '3ER. TURNO'), ('MIXTO', 'MIXTO')], default='1ER. TURNO', max_length=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Linea')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Supervisor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Tiempo Muerto',
                'verbose_name_plural': 'Encabezados Tiempos Muertos',
            },
        ),
        migrations.CreateModel(
            name='TiempoMuertonDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('obs', models.CharField(max_length=100, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('total_tm', models.FloatField(default=0)),
                ('causa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmuertos.CausaTM')),
                ('tiempo_muerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salidas.TiempoMuertoEnc')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Tiempo Muerto',
                'verbose_name_plural': 'Detalles Tiempos Muertos',
            },
        ),
        migrations.CreateModel(
            name='TiempoMuertoCongEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_produccion', models.DateField()),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('total_tm', models.FloatField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('turno', models.CharField(choices=[('TURNO 1', 'TURNO 1'), ('TURNO 2', 'TURNO 2'), ('TURNO 3', 'TURNO 3'), ('TURNO MIXTO', 'TURNO MIXTO'), ('TURNO APOYO', 'TURNO APOYO')], default='TURNO 1', max_length=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Linea')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Supervisor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Tiempo Muerto Cong',
                'verbose_name_plural': 'Encabezados Tiempos Muertos Cong',
            },
        ),
        migrations.CreateModel(
            name='TiempoMuertoCongDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('obs', models.CharField(max_length=100, null=True)),
                ('total_tm', models.FloatField(default=0)),
                ('causa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmuertos.CausaTM')),
                ('tiempo_muerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salidas.TiempoMuertoCongEnc')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Tiempo Muerto Cong',
                'verbose_name_plural': 'Detalles Tiempos Muertos Cong',
            },
        ),
        migrations.CreateModel(
            name='ProduccionEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_produccion', models.DateField()),
                ('ftm', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=2)),
                ('fpr', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=2)),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('total_produccion', models.FloatField(default=0)),
                ('total_utilizado', models.FloatField(default=0)),
                ('total_merma', models.FloatField(default=0)),
                ('peso', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('plantilla', models.IntegerField(default=0)),
                ('turno', models.CharField(choices=[('1ER. TURNO', '1ER. TURNO'), ('2DO. TURNO', '2DO. TURNO'), ('3ER. TURNO', '3ER. TURNO'), ('MIXTO', 'MIXTO')], default='1ER. TURNO', max_length=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Linea')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Operador')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Supervisor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Produccion',
                'verbose_name_plural': 'Encabezados Producciones',
            },
        ),
        migrations.CreateModel(
            name='ProduccionDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('tproducto', models.CharField(choices=[('PROCESO', 'PROCESO'), ('TERMINADO', 'TERMINADO')], default='TERMINADO', max_length=20)),
                ('peso', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('resto', models.FloatField(default=0)),
                ('velocidad', models.IntegerField(default=0)),
                ('total_produccion', models.FloatField(default=0)),
                ('total_utilizado', models.FloatField(default=0)),
                ('total_merma', models.FloatField(default=0)),
                ('produccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salidas.ProduccionEnc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Producto')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Produccion',
                'verbose_name_plural': 'Detalles Producciones',
            },
        ),
        migrations.CreateModel(
            name='ProduccionCongEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_produccion', models.DateField()),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
                ('total_produccion', models.FloatField(default=0)),
                ('total_utilizado', models.FloatField(default=0)),
                ('total_merma', models.FloatField(default=0)),
                ('peso', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('plantilla', models.IntegerField(default=0)),
                ('shift', models.CharField(choices=[('TURNO 1', 'TURNO 1'), ('TURNO 2', 'TURNO 2'), ('TURNO 3', 'TURNO 3'), ('TURNO MIXTO', 'TURNO MIXTO'), ('TURNO APOYO', 'TURNO APOYO')], max_length=30)),
                ('horas_turno', models.FloatField(default=8)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Linea')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Supervisor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Produccion cong',
                'verbose_name_plural': 'Encabezados Producciones Cong',
            },
        ),
        migrations.CreateModel(
            name='ProduccionCongDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('tproducto', models.CharField(choices=[('PROCESO', 'PROCESO'), ('TERMINADO', 'TERMINADO')], default='PROCESO', max_length=20)),
                ('peso', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('resto', models.FloatField(default=0)),
                ('total_produccion', models.FloatField(default=0)),
                ('total_utilizado', models.FloatField(default=0)),
                ('total_merma', models.FloatField(default=0)),
                ('r1', models.IntegerField(default=0)),
                ('r2', models.IntegerField(default=0)),
                ('r3', models.IntegerField(default=0)),
                ('r4', models.IntegerField(default=0)),
                ('r5', models.IntegerField(default=0)),
                ('produccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salidas.ProduccionCongEnc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Producto')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Produccion Cong',
                'verbose_name_plural': 'Detalles Producciones Cong',
            },
        ),
    ]
