# Generated by Django 2.0.4 on 2018-05-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_journals_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellvalue',
            name='journal_page',
        ),
        migrations.DeleteModel(
            name='CellValue',
        ),
        migrations.DeleteModel(
            name='JournalPage',
        ),
    ]
