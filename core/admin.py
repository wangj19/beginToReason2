"""
This module registers the models we created for the "core" application. After registering
the model, the data will be accessible through Django's admin functionality.
"""
from django.contrib import admin
from .models import Lesson, LessonSetLessons, MainSetLessonSets, Reference, Concept, Reasoning, McChoice, Question, Code, LessonSet, \
    Feedback, MainSet

# Register your models here.
admin.site.register(LessonSet)
admin.site.register(Lesson)
admin.site.register(Feedback)
admin.site.register(Reference)
admin.site.register(Concept)
admin.site.register(Reasoning)
admin.site.register(Question)
admin.site.register(McChoice)
admin.site.register(Code)
admin.site.register(MainSet)
admin.site.register(MainSetLessonSets)
admin.site.register(LessonSetLessons)