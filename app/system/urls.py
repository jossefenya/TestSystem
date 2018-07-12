from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailTaskView.as_view(), name='detail_task'),
    path('<int:task_id>/<int:pk>/', views.DetailQuestionView.as_view(), name='detail_question'),
    path('<int:task_id>/<int:question_id>/', views.vote, name='vote'),
]