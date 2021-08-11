# Generated by Django 3.0.4 on 2021-08-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_client_Interface_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pc_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='计算机名称')),
                ('board_serialNumber', models.CharField(max_length=2, verbose_name='主板序列号')),
                ('disk_serialNumber', models.CharField(blank=True, max_length=500, null=True, verbose_name='硬盘信息')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('change_add', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '物料编码大类',
            },
        ),
        migrations.DeleteModel(
            name='Pc',
        ),
    ]