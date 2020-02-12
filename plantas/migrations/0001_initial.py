# Generated by Django 2.2.6 on 2020-01-30 04:39

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
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripcion de Planta', max_length=100, unique=True)),
                ('id_planta', models.CharField(help_text='Clave o ID de la Planta', max_length=2, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Plantas',
            },
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Línea', max_length=100)),
                ('id_linea', models.CharField(help_text='Id Linea', max_length=4, unique=True)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Lineas',
                'unique_together': {('planta', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción del Supervisor', max_length=100, unique=True)),
                ('id_supervisor', models.CharField(help_text='Id Supervisor', max_length=4, unique=True)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Supervisores',
                'unique_together': {('planta', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción del Operador', max_length=100, unique=True)),
                ('id_operador', models.CharField(help_text='Id operador', max_length=4, unique=True)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Planta')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Operadores',
                'unique_together': {('planta', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Formadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Formadora', max_length=100)),
                ('id_formadora', models.CharField(help_text='Id Formadora', max_length=6, unique=True)),
                ('modelo', models.CharField(help_text='Modelo Formadora', max_length=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Linea')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Formadoras',
                'unique_together': {('linea', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Bascula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Báscula', max_length=100)),
                ('id_bascula', models.CharField(help_text='Id Bascula', max_length=6, unique=True)),
                ('celdas', models.IntegerField(default=0)),
                ('modelo', models.CharField(help_text='Modelo Báscula', max_length=20)),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.Linea')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Basculas',
                'unique_together': {('linea', 'descripcion')},
            },
        ),
    ]
