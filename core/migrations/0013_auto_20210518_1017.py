# Generated by Django 3.1.8 on 2021-05-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_lessonincorrectanswers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incorrectanswer',
            name='type',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='incorrect_answers',
        ),
    ]
