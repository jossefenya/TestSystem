from django.contrib import admin

from .models import Task, Question, Choice, User


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'user',)


    inlines = [QuestionInLine, ChoiceInLine, ]

admin.site.register(Task, TaskAdmin)

