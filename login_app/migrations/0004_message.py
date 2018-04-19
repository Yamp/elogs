# Generated by Django 2.0.3 on 2018-04-12 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20180410_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('type', models.CharField(choices=[('critical_value', 'Критическое значение'), ('note', 'Замечание')], max_length=10, null=True, verbose_name='Тип сообщения')),
                ('position', models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип сообщения')),
                ('addressee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='login_app.Employee')),
            ],
        ),
    ]
