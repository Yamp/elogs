# Generated by Django 2.0.7 on 2018-07-12 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fractional_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cindermeasurement',
            options={'verbose_name': 'Измерение гранулярного состава огарка', 'verbose_name_plural': 'Измерения гранулярного состава огарка'},
        ),
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='measurementpair',
            options={'verbose_name': 'Пара измерений', 'verbose_name_plural': 'Пары измерений'},
        ),
        migrations.AlterModelOptions(
            name='schiehtmeasurement',
            options={'verbose_name': 'Измерение гранулярного состава шихты', 'verbose_name_plural': 'Измерения гранулярного состава шихты'},
        ),
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['min_size'], 'verbose_name': 'Вес', 'verbose_name_plural': 'Веса'},
        ),
        migrations.AlterField(
            model_name='measurementpair',
            name='cinder',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pair', to='fractional_app.CinderMeasurement', verbose_name='Огарок'),
        ),
        migrations.AlterField(
            model_name='measurementpair',
            name='schieht',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pair', to='fractional_app.SchiehtMeasurement', verbose_name='Шихта'),
        ),
    ]