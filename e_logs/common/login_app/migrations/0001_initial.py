<<<<<<< HEAD
# Generated by Django 2.0.6 on 2018-08-10 15:47
=======
# Generated by Django 2.0.7 on 2018-08-10 15:59
>>>>>>> 8bee91f09c7f8ba19c68907116b07e1eeb91fbc2

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('all_journals_app', '0001_initial'),
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
                ('owned_shifts', models.ManyToManyField(blank=True, to='all_journals_app.Shift')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рабочий',
                'verbose_name_plural': 'Рабочие',
            },
        ),
    ]
