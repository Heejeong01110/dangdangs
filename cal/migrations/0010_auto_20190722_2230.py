# Generated by Django 2.2.3 on 2019-07-22 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0009_auto_20190721_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 22, 22, 30, 41, 505050)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 22, 22, 30, 41, 505050)),
        ),
    ]