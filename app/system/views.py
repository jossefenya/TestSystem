from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, render_to_response
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Task, Question, Choice
from .forms import MyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'system/index.html'
    context_object_name = 'latest_task_list'


    def get_queryset(self):
        return Task.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailTaskView(generic.DetailView):
    model = Task
    template_name = 'system/detail_task.html'


    def get_queryset(self):
        return Task.objects.filter(pub_date__lte=timezone.now())


class DetailQuestionView(generic.DetailView):
    model = Question
    template_name = 'system/detail_question.html'


def check_solution(request):
    form = MyForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            choice = request.POST["choice"]

    return render(request, 'system/detail_question.html', {'form': form})


def register(request):
    context = {}
    register_form = UserCreationForm()
    context = {'register_form': register_form}
    if request.method == "post" or request.method == "POST":
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return HttpResponseRedirect('/system/')
        else:
            register_form = new_user_form
            context = {'register_form': register_form}
    return render(request, 'system/register.html', context)
