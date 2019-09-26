# Generated by Django 2.2.5 on 2019-09-26 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0024_auto_20190925_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicuser',
            name='campus_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.Campus'),
        ),
        migrations.AddField(
            model_name='record',
            name='campus_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.Campus'),
        ),
    ]
