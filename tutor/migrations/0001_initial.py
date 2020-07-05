# Generated by Django 3.0.7 on 2020-07-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=30)),
                ('template_code', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=30)),
                ('lesson_code', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LessonSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_set_id', models.IntegerField()),
                ('lesson_set_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_key', models.CharField(max_length=30)),
                ('reference_text', models.TextField(max_length=250)),
                ('lesson', models.ManyToManyField(related_name='references', to='tutor.Lesson')),
            ],
        ),
    ]
