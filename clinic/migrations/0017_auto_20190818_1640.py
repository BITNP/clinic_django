# Generated by Django 2.2.4 on 2019-08-18 08:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0016_announcement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='expireTime',
        ),
        migrations.AddField(
            model_name='announcement',
            name='expireDate',
            field=models.DateField(default=datetime.datetime(2019, 8, 18, 8, 40, 31, 670321, tzinfo=utc), verbose_name='失效时间'),
            preserve_default=False,
        ),
    ]
