# Generated by Django 2.2.4 on 2019-08-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_auto_20190816_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='已使用容量'),
            preserve_default=False,
        ),
    ]