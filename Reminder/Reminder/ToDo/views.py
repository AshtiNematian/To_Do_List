from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from ToDo.serializer import TaskSerrializer

from ToDo.models import Task, Categories


class HomePageView(TemplateView):
    template_name = 'base.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'categories_detail.html'


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = {'expire_list': Task.objects.expire_task().all(),
                    'going_list': Task.objects.going_task().all()}
        return queryset


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = '__all__'
    success_url = reverse_lazy('task_new')


class CategoryListView(ListView):
    model = Categories
    template_name = 'categories.html'
    context_object_name = "categories"

    def get_queryset(self):
        queryset = {'empty_list': Categories.object.empty().all(),
                    'non_empty_list': Categories.object.non_empty().all()}
        return queryset


def task_detail(resquest):
    tsk = Task.objects.all()
    serializer = TaskSerrializer(tsk, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
