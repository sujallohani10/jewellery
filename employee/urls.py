from django.urls import path

from . import views

urlpatterns = [
    path('task/add', views.addEmployeeTask, name='employeeTask'),
    path('task/', views.employeeTaskList, name='employeeTaskList'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]