# Generated by Django 3.1.1 on 2020-09-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userinformation_completed_sets'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='mood',
            field=models.CharField(choices=[('NEU', 'Neutral'), ('HAP', 'Happy'), ('EXC', 'Excited'), ('UPS', 'Upset'), ('SAD', 'Sad')], default='NEU', max_length=3),
        ),
    ]
