# Generated by Django 2.1.2 on 2018-10-24 05:21

from django.db import migrations, models
import e_logs.core.utils.webutils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, max_length=200, null=True, verbose_name='Тема')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Сообщение')),
                ('plant', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цех')),
                ('url', models.CharField(blank=True, max_length=256, null=True, verbose_name='URL')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Почта')),
                ('filenames', models.TextField(default='', verbose_name='Имена файлов')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Пользователь')),
            ],
            bases=(e_logs.core.utils.webutils.StrAsDictMixin, models.Model),
        ),
    ]
