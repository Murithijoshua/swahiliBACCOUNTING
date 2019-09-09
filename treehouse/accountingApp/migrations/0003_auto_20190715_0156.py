# Generated by Django 2.2.3 on 2019-07-15 01:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accountingApp', '0002_auto_20190715_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='purpose',
            field=models.CharField(default=django.utils.timezone.now, max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 1, 55, 53, 515500, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 1, 55, 53, 515677, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date_of_purchase',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 1, 55, 53, 528099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sale',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 1, 55, 53, 527601, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sale',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 1, 55, 53, 527676, tzinfo=utc)),
        ),
    ]
