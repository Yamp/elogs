# Generated by Django 2.0.4 on 2018-04-27 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('shift', 'Смена'), ('equipment', 'Оборудование'), ('month', 'Месяц')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_name', models.CharField(max_length=256, verbose_name='Название журнала')),
                ('table_name', models.CharField(max_length=128, verbose_name='Название таблицы')),
                ('field_id', models.CharField(max_length=128, verbose_name='Название поля')),
                ('index', models.IntegerField(blank=True, default=None, null=True)),
                ('value', models.CharField(max_length=1024, verbose_name='Минимальный размер')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to='all_journals_app.Objects')),
            ],
        ),
    ]
