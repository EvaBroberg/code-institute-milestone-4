# Generated by Django 3.0.4 on 2020-05-03 22:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20200503_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 22, 13, 11, 567399, tzinfo=utc)),
        ),
    ]
