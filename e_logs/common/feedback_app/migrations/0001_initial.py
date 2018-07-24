# Generated by Django 2.0.5 on 2018-07-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200, verbose_name='Тема')),
                ('text', models.CharField(max_length=1000, verbose_name='Сообщение')),
                ('plant', models.CharField(max_length=50, verbose_name='Цех')),
                ('journal', models.CharField(max_length=256, verbose_name='Журнал')),
                ('email', models.CharField(max_length=200, verbose_name='Почта')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Пользователь')),
            ],
        ),
    ]
