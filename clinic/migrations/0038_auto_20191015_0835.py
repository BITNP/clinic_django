# Generated by Django 2.2.4 on 2019-10-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0037_auto_20191014_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='brief',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='内容概括'),
        ),
    ]
