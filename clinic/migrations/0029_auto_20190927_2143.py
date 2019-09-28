# Generated by Django 2.2.4 on 2019-09-27 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0028_auto_20190926_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='endTime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='服务结束时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='date',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='服务开始时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campus',
            name='name',
            field=models.CharField(max_length=10, unique=True, verbose_name='校区名称'),
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(verbose_name='开始日期'),
        ),
    ]