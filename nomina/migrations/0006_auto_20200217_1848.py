# Generated by Django 2.2.6 on 2020-02-18 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0005_nominaenc_plantilla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominadet',
            name='cantidad',
            field=models.FloatField(default=0.0),
        ),
    ]
