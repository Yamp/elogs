# Generated by Django 2.0.6 on 2018-07-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180726_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='value',
            field=models.CharField(max_length=512, verbose_name='Значение'),
        ),
    ]