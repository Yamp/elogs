# Generated by Django 2.1.2 on 2018-10-12 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import e_logs.core.utils.webutils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('position', models.CharField(blank=True, choices=[('master', 'Мастер'), ('laborant', 'Лаборант'), ('hydro', 'Аппаратчик-гидрометаллург'), ('admin', 'Админ'), ('boss', 'Начальник цеха')], max_length=128)),
                ('plant', models.CharField(choices=[('furnace', 'Обжиг'), ('leaching', 'Выщелачивание'), ('electrolysis', 'Электролиз')], max_length=128, null=True, verbose_name='Цех')),
                ('csrf', models.CharField(default=' ', max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рабочий',
                'verbose_name_plural': 'Рабочие',
            },
            bases=(e_logs.core.utils.webutils.StrAsDictMixin, models.Model),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['plant', 'position'], name='login_app_e_plant_2940c7_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['plant'], name='login_app_e_plant_70993a_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['position'], name='login_app_e_positio_8631f6_idx'),
        ),
    ]
