# Generated by Django 2.0.6 on 2018-07-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('value', models.CharField(max_length=128, verbose_name='Значение')),
                ('plant', models.CharField(blank=True, max_length=128, null=True, verbose_name='Цех')),
                ('journal', models.CharField(blank=True, max_length=128, null=True, verbose_name='Журнал')),
                ('table', models.CharField(blank=True, max_length=128, null=True, verbose_name='Таблица')),
                ('cell', models.CharField(blank=True, max_length=128, null=True, verbose_name='Ячейка')),
            ],
        ),
    ]
