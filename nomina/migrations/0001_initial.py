# Generated by Django 2.2.6 on 2020-02-21 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaNomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('id_area', models.CharField(max_length=4, unique=True)),
                ('descripcion_area', models.CharField(max_length=20, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Areas Nomina',
            },
        ),
        migrations.CreateModel(
            name='ConceptoNomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('id_concepto', models.CharField(max_length=100)),
                ('concepto', models.CharField(max_length=100, unique=True)),
                ('tipo_concepto', models.CharField(blank=True, choices=[('PERCEPCION', 'PERCEPCION'), ('DEDUCCION', 'DEDUCCION')], max_length=30, null=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='lineaNomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('id_linea', models.CharField(max_length=4, unique=True)),
                ('descripcion_linea', models.CharField(max_length=20, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Lineas Nomina',
            },
        ),
        migrations.CreateModel(
            name='SupervisorNomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('id_supervisor', models.CharField(max_length=4, unique=True)),
                ('nombre_supervisor', models.CharField(max_length=100, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Supervisores Nomina',
            },
        ),
        migrations.CreateModel(
            name='PlantaNomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('id_planta', models.CharField(max_length=2, unique=True)),
                ('descripcion_planta', models.CharField(max_length=20, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Plantas Nomina',
            },
        ),
        migrations.CreateModel(
            name='NominaEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_nomina', models.DateField()),
                ('grupo', models.CharField(blank=True, choices=[('PERSONAL', 'PERSONAL'), ('SUPERVISOR', 'SUPERVISOR'), ('AUXILIAR', 'AUXILIAR')], max_length=30, null=True)),
                ('semana', models.IntegerField(default=1)),
                ('plantilla', models.IntegerField(default=0)),
                ('total_percepciones', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('total_deducciones', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.AreaNomina', to_field='descripcion_area')),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.lineaNomina', to_field='descripcion_linea')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.PlantaNomina', to_field='descripcion_planta')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.SupervisorNomina', to_field='nombre_supervisor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Nomina',
                'verbose_name_plural': 'Encabezados Nomina',
            },
        ),
        migrations.CreateModel(
            name='NominaDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.FloatField(default=0.0)),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.ConceptoNomina', to_field='concepto')),
                ('nomina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.NominaEnc')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Nomina',
                'verbose_name_plural': 'Detalles Nomina',
            },
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('grupo', models.CharField(blank=True, choices=[('PERSONAL', 'PERSONAL'), ('SUPERVISOR', 'SUPERVISOR'), ('AUXILIAR', 'AUXILIAR')], max_length=30, null=True)),
                ('semana', models.IntegerField(default=1)),
                ('cantidad', models.FloatField(default=0.0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.AreaNomina')),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.ConceptoNomina')),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.lineaNomina')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.PlantaNomina')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomina.SupervisorNomina')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
