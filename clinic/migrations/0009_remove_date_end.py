# Generated by Django 2.2.4 on 2019-08-16 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_auto_20190816_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='end',
        ),
    ]
