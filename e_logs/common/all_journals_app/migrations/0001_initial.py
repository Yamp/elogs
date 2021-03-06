# Generated by Django 2.1.2 on 2018-10-24 06:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('index', models.IntegerField(default=None, verbose_name='Номер строчки')),
                ('value', models.CharField(blank=True, default='', max_length=1024, verbose_name='Значение поля')),
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
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=2048, verbose_name='Текст комментария')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Столбец')),
                ('formula', models.CharField(default='', max_length=4000, null=True, verbose_name='Формула')),
                ('verbose_name', models.CharField(max_length=256, verbose_name='Название столбца')),
                ('type', models.CharField(default='', max_length=128, null=True)),
                ('units', models.CharField(default='', max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Поле',
                'verbose_name_plural': 'Поля',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Журнал')),
                ('verbose_name', models.CharField(max_length=256, verbose_name='Название журнала')),
                ('type', models.CharField(choices=[('shift', 'Смена'), ('equipment', 'Оборудование'), ('measurement', 'Измерение'), ('month', 'Месяц'), ('year', 'Год')], default='shift', max_length=128, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('leaching', 'Выщелачивание'), ('furnace', 'Обжиг'), ('electrolysis', 'Электролиз')], default='leaching', max_length=128, verbose_name='Цех')),
                ('verbose_name', models.CharField(max_length=128, verbose_name='Название цеха')),
            ],
            options={
                'verbose_name': 'Цех',
                'verbose_name_plural': 'Цеха',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Таблица')),
                ('verbose_name', models.CharField(max_length=256, verbose_name='Название таблицы')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='all_journals_app.Journal')),
            ],
            options={
                'verbose_name': 'Таблица',
                'verbose_name_plural': 'Таблицы',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('cellgroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='all_journals_app.CellGroup')),
                ('name', models.CharField(default='', max_length=1024, verbose_name='Название оборудования')),
            ],
            bases=('all_journals_app.cellgroup',),
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
                ('order', models.IntegerField(verbose_name='Номер смены')),
                ('date', models.DateField(verbose_name='Дата начала смены')),
                ('closed', models.BooleanField(default=False)),
                ('ended', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Смена',
                'verbose_name_plural': 'Смены',
            },
            bases=('all_journals_app.cellgroup',),
        ),
        migrations.AddField(
            model_name='journal',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journals', to='all_journals_app.Plant'),
        ),
        migrations.AddField(
            model_name='field',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='all_journals_app.Table'),
        ),
    ]
