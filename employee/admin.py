from django.contrib import admin
from employee.models import Employee, EmployeeTasks


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'address', 'birth_date', 'contact_info', 'profile_photo', 'status', 'joined_date')


class EmployeeTasksAdmin(admin.ModelAdmin):
    list_display = (
        'employee_id', 'item', 'description', 'gold_weight', 'silver_weight', 'bronze_weight', 'given_date', 'completion_date')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeTasks, EmployeeTasksAdmin)
