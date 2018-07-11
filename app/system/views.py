from django.shortcuts import render, HttpResponse, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Task, Question, Choice
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
"""
def index(request):
    latest_task_list = Task.objects.order_by('-pub_date')[:10]
    context = {'latest_task_list': latest_task_list}
    return render(request, 'system/index.html', context)


def detail_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task doesn't exist")
    return render(request, 'system/detail_task.html', {'task': task})
"""



def detail_question(request, task_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'system/detail_question.html', {'question': question})


def vote(request, question_id):
    question_count = 0
    question = get_object_or_404(Question, pk=question_id)
    max_question = question.objects.all()
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    return HttpResponseRedirect('index.html')
