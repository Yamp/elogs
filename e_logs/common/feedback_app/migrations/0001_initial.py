# Generated by Django 2.1.2 on 2018-10-12 09:51

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
                ('theme', models.CharField(max_length=200, verbose_name='Тема')),
                ('text', models.CharField(max_length=1000, verbose_name='Сообщение')),
                ('plant', models.CharField(max_length=50, verbose_name='Цех')),
                ('journal', models.CharField(max_length=256, verbose_name='Журнал')),
                ('email', models.CharField(max_length=200, verbose_name='Почта')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Пользователь')),
            ],
            bases=(e_logs.core.utils.webutils.StrAsDictMixin, models.Model),
        ),
    ]
