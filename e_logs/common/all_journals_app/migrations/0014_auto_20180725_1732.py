# Generated by Django 2.0.6 on 2018-07-25 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all_journals_app', '0013_auto_20180724_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpage',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='all_journals_app.Plant', verbose_name='Цех'),
        ),
        migrations.AlterUniqueTogether(
            name='journalpage',
            unique_together=set(),
        ),
    ]
