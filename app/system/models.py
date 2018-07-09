from django.db import models
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=128, help_text="Enter the name")

    def __str__(self):
        return self.task_name



class Question(models.Model):
    question_name = models.CharField(max_length=128, help_text="Enter the name")

    task = models.ForeignKey(Task, on_delete=models.CASCADE)


    def __str__(self):
        return self.question_name


class Choice(models.Model):
    choice_name = models.CharField(max_length=128, help_text="Enter the name")
    is_true = models.BooleanField(default=False)

    question = models.ManyToManyField(Question)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


    def __str__(self):
        return self.choice_name

