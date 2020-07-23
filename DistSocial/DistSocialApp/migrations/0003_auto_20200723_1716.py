# Generated by Django 3.0.3 on 2020-07-23 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DistSocialApp', '0002_auto_20200723_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catcamaras',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='catlocalidades',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='catorganizaciones',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='cattipos',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='catusuarios',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='registros',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
