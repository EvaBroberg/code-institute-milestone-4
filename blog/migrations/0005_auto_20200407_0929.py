# Generated by Django 3.0.4 on 2020-04-07 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200322_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 7, 9, 29, 47, 223153, tzinfo=utc)),
        ),
    ]