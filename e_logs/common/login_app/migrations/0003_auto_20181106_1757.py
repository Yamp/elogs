# Generated by Django 2.1.3 on 2018-11-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20181026_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='plant',
            field=models.CharField(blank=True, choices=[('furnace', 'Обжиг'), ('leaching', 'Выщелачивание'), ('electrolysis', 'Электролиз'), (None, '-')], max_length=128, null=True, verbose_name='Цех'),
        ),
    ]