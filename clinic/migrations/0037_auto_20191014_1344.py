# Generated by Django 2.2.4 on 2019-10-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0036_auto_20191012_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='is_appointment',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='tag',
            field=models.CharField(choices=[('AN', '普通公告'), ('TOC', '免责声明'), ('TA', '置顶公告')], max_length=16, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=20, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='address',
            field=models.CharField(max_length=128, verbose_name='诊所地址'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='校区名称'),
        ),
        migrations.AlterField(
            model_name='clinicuser',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码'),
        ),
        migrations.AlterField(
            model_name='date',
            name='title',
            field=models.CharField(default='正常服务', max_length=20, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='record',
            name='description',
            field=models.CharField(max_length=600, verbose_name='问题自述'),
        ),
        migrations.AlterField(
            model_name='record',
            name='method',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='处理方法'),
        ),
        migrations.AlterField(
            model_name='record',
            name='model',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='电脑型号'),
        ),
        migrations.AlterField(
            model_name='record',
            name='password',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='record',
            name='phone_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码'),
        ),
        migrations.AlterField(
            model_name='record',
            name='reject_reason',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='拒绝理由'),
        ),
        migrations.AlterField(
            model_name='record',
            name='worker_description',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='问题描述'),
        ),
    ]