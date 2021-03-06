# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-06 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forwarder', '0003_auto_20171105_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='hierarchy',
            name='application_type',
        ),
        migrations.AddField(
            model_name='hierarchy',
            name='name',
            field=models.CharField(default='HA01', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationtype',
            name='hierarchy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forwarder.Hierarchy'),
        ),
    ]
