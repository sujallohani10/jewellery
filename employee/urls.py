from django.urls import path

from . import views

urlpatterns = [
    path('task/add', views.employeeTask, name='employeeTask'),
]