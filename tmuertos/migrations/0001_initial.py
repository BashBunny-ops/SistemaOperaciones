# Generated by Django 2.2.6 on 2020-02-13 15:46

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
            name='CategoriaTM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('id_categoriaTM', models.CharField(max_length=4, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CategoriasTM',
            },
        ),
        migrations.CreateModel(
            name='CausaTM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Categoría', max_length=100, unique=True)),
                ('id_causaTM', models.CharField(help_text='Id Causa TM', max_length=4, unique=True)),
                ('tipo', models.CharField(choices=[('Programado', 'Programado'), ('No Programado', 'No Programado'), ('Imprevisto', 'Imprevisto')], default='Programado', max_length=15)),
                ('tolerancia', models.IntegerField(default=0)),
                ('categoriaTM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmuertos.CategoriaTM')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CausasTM',
                'unique_together': {('categoriaTM', 'descripcion')},
            },
        ),
    ]
