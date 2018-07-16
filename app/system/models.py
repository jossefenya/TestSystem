from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=128, help_text="Enter the name")
    pub_date = models.DateTimeField('Date', default=None)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

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

    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


    def __str__(self):
        return self.choice_name

