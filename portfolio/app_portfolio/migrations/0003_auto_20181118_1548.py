# Generated by Django 2.1.1 on 2018-11-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0002_proyecto_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='frontpage',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='empresa',
            field=models.CharField(max_length=64, verbose_name='Empresa'),
        ),
    ]
