from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EmployeeTaskForm
from employee.models import EmployeeTasks


def employeeTask(request):
    if request.method == 'POST':
        form = EmployeeTaskForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            item = form.cleaned_data['item']
            desc = form.cleaned_data['description']
            gold_weight = form.cleaned_data['gold_weight']
            silver_weight = form.cleaned_data['silver_weight']
            bronze_weight = form.cleaned_data['bronze_weight']
            task_given_date = form.cleaned_data['task_given_date']
            completion_date = form.cleaned_data['completion_date']
            emp_task_obj = EmployeeTasks(item=item, description=desc, gold_weight=gold_weight,
                                         silver_weight=silver_weight, bronze_weight=bronze_weight,
                                         given_date=task_given_date, completion_date=completion_date)  # get the data into the employeetask model
            emp_task_obj.save()

            return HttpResponseRedirect('/employee/task')
    else:
        form = EmployeeTaskForm()
    return render(request, 'employee/task.html', {'form': form})
