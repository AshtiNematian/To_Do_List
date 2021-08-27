from datetime import datetime
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class CatManager(models.Manager):
    def empty(self):
        return Categories.objects.filter(categor__isnull=True)

    def non_empty(self):
        return Categories.objects.filter(categor__isnull=False)


class Categories(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    objects = models.Manager()
    object = CatManager()

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'


class TaskManager(models.Manager):
    def expire_task(self):
        ex_task = Task.objects.filter(date_of_task__lt=timezone.now())
        return ex_task

    def going_task(self):
        ex_task = Task.objects.filter(date_of_task__gte=timezone.now())
        return ex_task


class Task(models.Model):
    PRIORITY = [('Necessary', 'Necessary'), ('Normal', 'Normal'), ('Poor Priority', 'Poor Priority'), ]
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categor')
    priority = models.CharField(choices=PRIORITY, max_length=20, null=True, blank=True, default='Normal')
    date_of_task = models.DateTimeField()
    date_create = models.DateTimeField(default=datetime.now)
    active_task = models.BooleanField(default=True)
    objects = TaskManager()
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ['date_of_task']

    @property
    def age(self):
        return self.date_of_task - self.date_create

    def get_absolute_url(self):
        return reverse('task', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'
