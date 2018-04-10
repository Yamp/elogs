# Generated by Django 2.0.3 on 2018-04-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='plant',
            field=models.CharField(choices=[('furnace', 'обжиг'), ('leaching', 'выщелачивание'), ('electrolysis', 'электролиз')], max_length=10, null=True, verbose_name='Цех'),
        ),
    ]
