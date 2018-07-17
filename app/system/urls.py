from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailTaskView.as_view(), name='detail_task'),
    path('<int:task_id>/<int:pk>/', views.DetailQuestionView.as_view(), name='detail_question'),
    path('register/', views.register, name='register'),
    path('results/', views.check_solution, name='results')
]