# Generated by Django 3.1.2 on 2021-02-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210222_1519'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='completed_sets',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='completed_sets',
            field=models.ManyToManyField(blank=True, null=True, related_name='sets_completed', to='core.MainSet'),
        ),
    ]
