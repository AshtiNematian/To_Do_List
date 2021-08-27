from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tasksdetail/<slug:slug>/',
         TaskDetailView.as_view(), name='task'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('Task/', TaskListView.as_view(), name='task_list'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categoriesdetail/<slug:slug>/', CategoriesDetailView.as_view(), name='category'),
    path('taskserializer/', views.task_detail, name='serialtask')
]
