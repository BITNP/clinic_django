# Generated by Django 2.2.5 on 2019-09-26 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0027_auto_20190926_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinicuser',
            old_name='campus_link',
            new_name='campus',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='campus_link',
            new_name='campus',
        ),
    ]
