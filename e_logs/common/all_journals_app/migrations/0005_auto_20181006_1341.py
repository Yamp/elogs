# Generated by Django 2.1 on 2018-10-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all_journals_app', '0004_auto_20181006_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to='contenttypes.ContentType'),
        ),
    ]
