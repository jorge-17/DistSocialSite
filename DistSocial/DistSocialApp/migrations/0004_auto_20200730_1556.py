# Generated by Django 3.0.3 on 2020-07-30 20:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DistSocialApp', '0003_auto_20200723_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 20, 56, 21, 402139, tzinfo=utc), null=True),
        ),
    ]
