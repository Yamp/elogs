# Generated by Django 2.0.6 on 2018-07-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180727_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=2048, verbose_name='Значение'),
        ),
    ]
