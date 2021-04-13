# Generated by Django 3.1.8 on 2021-04-13 00:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_class', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Class')),
            ],
        ),
    ]