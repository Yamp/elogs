# Generated by Django 2.0.6 on 2018-08-07 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=128, verbose_name='Название таблицы')),
                ('field_name', models.CharField(max_length=128, verbose_name='Название поля')),
                ('index', models.IntegerField(default=None, verbose_name='Номер строчки')),
                ('value', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Значение поля')),
                ('comment', models.CharField(max_length=1024, null=True, verbose_name='Комментарий к ячейке')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='CellGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Значение поля')),
                ('type', models.CharField(choices=[('shift', 'Смена'), ('equipment', 'Оборудование'), ('measurement', 'Измерение'), ('month', 'Месяц'), ('year', 'Год')], max_length=128, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('leaching', 'Выщелачивание'), ('furnace', 'Обжиг'), ('electrolysis', 'Электролиз')], default='leaching', max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Цех',
                'verbose_name_plural': 'Цеха',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('cellgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='all_journals_app.CellGroup')),
                ('time', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала смены')),
            ],
            bases=('all_journals_app.cellgroup',),
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('cellgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='all_journals_app.CellGroup')),
                ('shift_order', models.IntegerField(blank=True, null=True, verbose_name='Номер смены')),
                ('shift_date', models.DateField(blank=True, null=True, verbose_name='Дата начала смены')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
            bases=('all_journals_app.cellgroup',),
        ),
        migrations.AddField(
            model_name='cellgroup',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_journals_app.Plant', verbose_name='Цех'),
        ),
        migrations.AddField(
            model_name='cell',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_journals_app.CellGroup'),
        ),
    ]
