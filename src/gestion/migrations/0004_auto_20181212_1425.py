# Generated by Django 2.1.4 on 2018-12-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20181212_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='estadoactivo',
            field=models.IntegerField(default=0),
        ),
    ]