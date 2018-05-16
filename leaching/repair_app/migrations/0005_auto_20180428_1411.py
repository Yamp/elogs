# Generated by Django 2.0.4 on 2018-04-28 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repair_app', '0004_auto_20180413_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairs',
            name='date_performed',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выполненных работ'),
        ),
        migrations.AlterField(
            model_name='repairs',
            name='comment',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Объем выполненных работ по устранению неисправностей'),
        ),
    ]