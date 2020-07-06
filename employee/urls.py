from django.urls import path

from . import views

urlpatterns = [
    path('task/add', views.employeeTask, name='employeeTask'),
    path('task/', views.employeeTaskList, name='employeeTaskList'),
]