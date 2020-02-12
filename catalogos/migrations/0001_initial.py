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
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_cliente', models.CharField(help_text='Descripción', max_length=100, unique=True)),
                ('id_cliente', models.CharField(help_text='Clave o ID  ', max_length=4, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_prod', models.CharField(help_text='Descripción', max_length=100, unique=True)),
                ('id_producto', models.CharField(help_text='Clave o ID   ', max_length=15, unique=True)),
                ('peso_caja', models.FloatField(default=0.0)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_presenta', models.CharField(help_text='Descripción', max_length=20, unique=True)),
                ('id_presentacion', models.CharField(help_text='Clave o ID', max_length=5, unique=True)),
                ('paqs', models.IntegerField(default=0)),
                ('peso', models.FloatField(default=0)),
                ('unidad', models.CharField(choices=[('LBS', 'LBS'), ('KG', 'KG'), ('GR', 'GR'), ('OZ', 'OZ')], default='OZ', help_text='Unidad de Medida  ', max_length=3)),
                ('peso_caja', models.FloatField(default=0.0)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Presentaciones',
            },
        ),
        migrations.CreateModel(
            name='Ingred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_ing', models.CharField(help_text='Descripción', max_length=100, unique=True)),
                ('id_ingred', models.CharField(help_text='Clave o ID   ', max_length=2, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ingreds',
            },
        ),
        migrations.CreateModel(
            name='Corte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_corte', models.CharField(help_text='Descripción', max_length=100, unique=True)),
                ('id_corte', models.CharField(help_text='Clave o ID  ', max_length=2, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cortes',
            },
        ),
        migrations.CreateModel(
            name='CasoEsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_ce', models.CharField(help_text='Descripción', max_length=100, unique=True)),
                ('id_ce', models.CharField(help_text='Clave o ID  ', max_length=2, unique=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Casos Espeiales',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('descripcion_marca', models.CharField(help_text='Descripción', max_length=100, unique=True)),
                ('id_marca', models.CharField(help_text='Clave o ID   ', max_length=4, unique=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Cliente')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
                'unique_together': {('cliente', 'descripcion_marca')},
            },
        ),
    ]
