# Generated by Django 2.0.2 on 2018-03-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express_anal_app', '0014_auto_20180312_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neutraldenser',
            name='num',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
