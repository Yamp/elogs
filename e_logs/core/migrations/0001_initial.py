# Generated by Django 2.0.6 on 2018-08-13 17:52

from django.db import migrations, models
import django.db.models.deletion
import e_logs.core.utils.webutils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('value', models.CharField(max_length=2048, verbose_name='Значение')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login_app.Employee')),
            ],
            bases=(e_logs.core.utils.webutils.StrAsDictMixin, models.Model),
        ),
        migrations.AddIndex(
            model_name='setting',
            index=models.Index(fields=['name', 'employee'], name='core_settin_name_e38cb3_idx'),
        ),
        migrations.AddIndex(
            model_name='setting',
            index=models.Index(fields=['name'], name='core_settin_name_b329f4_idx'),
        ),
        migrations.AddIndex(
            model_name='setting',
            index=models.Index(fields=['name', 'content_type', 'object_id'], name='core_settin_name_f9b029_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='setting',
            unique_together={('name', 'employee', 'content_type', 'object_id')},
        ),
    ]
