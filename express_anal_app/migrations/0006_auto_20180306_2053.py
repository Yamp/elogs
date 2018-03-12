# Generated by Django 2.0.2 on 2018-03-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express_anal_app', '0005_auto_20180306_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denseranal',
            name='sink',
            field=models.CharField(choices=[('ls', 'НС'), ('hs', 'ВС')], max_length=5, verbose_name='Слив'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='plant',
            field=models.CharField(choices=[('furnace', 'обжиг'), ('leaching', 'выщелачивание'), ('electrolysis', 'электролиз')], max_length=1, verbose_name='Цех'),
        ),
    ]