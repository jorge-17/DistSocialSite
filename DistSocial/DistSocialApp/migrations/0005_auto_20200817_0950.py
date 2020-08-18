# Generated by Django 3.0.3 on 2020-08-17 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DistSocialApp', '0004_auto_20200730_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 14, 50, 41, 950213, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='registros',
            name='valor',
            field=models.DecimalField(decimal_places=3, max_digits=12, null=True),
        ),
    ]
