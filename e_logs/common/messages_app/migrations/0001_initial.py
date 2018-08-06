# Generated by Django 2.0.6 on 2018-08-06 10:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
        ('all_journals_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('critical_value', 'Критическое значение'), ('comment', 'Замечание')], max_length=100, null=True, verbose_name='Тип сообщения')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('link', models.URLField(default='#', max_length=128, verbose_name='Ссылка на ячейку')),
                ('addressee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_adressee', to='login_app.Employee')),
                ('cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='all_journals_app.Cell')),
                ('sendee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages_sendee', to='login_app.Employee')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
