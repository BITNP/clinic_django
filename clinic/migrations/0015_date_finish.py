# Generated by Django 2.2.4 on 2019-08-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0014_auto_20190817_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='finish',
            field=models.PositiveIntegerField(default=0, verbose_name='已完成数量'),
        ),
    ]