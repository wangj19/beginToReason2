# Generated by Django 3.1.2 on 2021-02-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210113_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='user_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
