# Generated by Django 3.1.8 on 2021-05-09 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210509_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonset',
            name='first_in_set',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.PROTECT, to='core.lesson'),
            preserve_default=False,
        ),
    ]