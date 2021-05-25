# Generated by Django 3.1.8 on 2021-05-09 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210509_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonSetLessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.lesson')),
                ('lesson_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lessonset')),
            ],
        ),
        migrations.CreateModel(
            name='MainSetLessonSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('lesson_set', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.lessonset')),
                ('main_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mainset')),
            ],
        ),
        migrations.DeleteModel(
            name='LessonIndex',
        ),
    ]
