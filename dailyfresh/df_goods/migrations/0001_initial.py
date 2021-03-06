# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20, verbose_name='名称')),
                ('gpic', models.ImageField(upload_to='df_goods', verbose_name='图片')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格')),
                ('isDelete', models.BooleanField(default=False, verbose_name='删除')),
                ('gunit', models.CharField(max_length=20, verbose_name='类别')),
                ('gclick', models.IntegerField(verbose_name='点击量')),
                ('gstores', models.IntegerField(verbose_name='库存')),
                ('gsold', models.IntegerField(verbose_name='销售数量')),
                ('gtips', models.CharField(max_length=100, verbose_name='简介')),
                ('gcomment', models.CharField(max_length=200, verbose_name='评论')),
                ('gcontent', tinymce.models.HTMLField(verbose_name='宝贝详情')),
                ('gpush', models.BooleanField(default=False, verbose_name='推荐')),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='类别')),
                ('isDelete', models.BooleanField(default=False, verbose_name='删除')),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypeInfo', verbose_name='类别'),
        ),
    ]
