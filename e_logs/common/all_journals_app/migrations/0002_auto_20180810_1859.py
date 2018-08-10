# Generated by Django 2.0.7 on 2018-08-10 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
        ('all_journals_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.Employee'),
        ),
        migrations.AddField(
            model_name='cellgroup',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_journals_app.Journal'),
        ),
        migrations.AddField(
            model_name='cell',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_journals_app.Field'),
        ),
        migrations.AddField(
            model_name='cell',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='all_journals_app.CellGroup'),
        ),
        migrations.AddField(
            model_name='cell',
            name='responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login_app.Employee'),
        ),
        migrations.AlterUniqueTogether(
            name='cell',
            unique_together={('field', 'index', 'group')},
        ),
    ]
