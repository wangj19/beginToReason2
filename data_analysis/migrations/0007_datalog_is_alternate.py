# Generated by Django 3.1.8 on 2021-05-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analysis', '0006_remove_datalog_past_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalog',
            name='is_alternate',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
