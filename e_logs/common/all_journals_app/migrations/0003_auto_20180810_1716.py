# Generated by Django 2.0.7 on 2018-08-10 14:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('all_journals_app', '0002_auto_20180809_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=2048, verbose_name='Текст комментария')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.Employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='cell',
            name='comment',
        ),
        migrations.AlterField(
            model_name='cell',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='all_journals_app.CellGroup'),
        ),
    ]
