# Generated by Django 3.0.4 on 2020-05-05 12:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20200505_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 12, 5, 54, 791734, tzinfo=utc)),
        ),
    ]
