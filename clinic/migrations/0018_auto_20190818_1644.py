# Generated by Django 2.2.4 on 2019-08-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0017_auto_20190818_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='tag',
            field=models.CharField(max_length=5, verbose_name='类型'),
        ),
    ]