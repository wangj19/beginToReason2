# Generated by Django 3.1.8 on 2021-04-13 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0002_datalog_class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datalog',
            old_name='class_id',
            new_name='class_key',
        ),
    ]
