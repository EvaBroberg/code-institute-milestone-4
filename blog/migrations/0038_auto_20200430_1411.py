# Generated by Django 3.0.4 on 2020-04-30 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20200429_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 14, 11, 41, 16597, tzinfo=utc)),
        ),
    ]