# Generated by Django 3.0.4 on 2020-04-24 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20200424_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 12, 51, 36, 350565, tzinfo=utc)),
        ),
    ]