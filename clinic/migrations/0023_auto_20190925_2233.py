# Generated by Django 2.2.5 on 2019-09-25 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0022_date_campus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='name',
            new_name='title',
        ),
    ]