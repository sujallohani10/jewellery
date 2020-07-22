from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import EmployeeTaskForm
from employee.models import EmployeeTasks


# Add Task
@login_required(login_url='/accounts/login')
def addEmployeeTask(request):
    if request.method == 'POST':
        form = EmployeeTaskForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the data in form.cleaned_data
            employee = form.cleaned_data['employee']
            item = form.cleaned_data['item']
            desc = form.cleaned_data['description']
            image = form.cleaned_data['image']
            gold_weight = form.cleaned_data['gold_weight']
            silver_weight = form.cleaned_data['silver_weight']
            bronze_weight = form.cleaned_data['bronze_weight']
            given_date = form.cleaned_data['given_date']
            completion_date = form.cleaned_data['completion_date']
            emp_task_obj = EmployeeTasks(employee=employee, item=item, description=desc, gold_weight=gold_weight,
                                         silver_weight=silver_weight, bronze_weight=bronze_weight,
                                         given_date=given_date,
                                         completion_date=completion_date, image=image)  # get the data into the employeetask model
            emp_task_obj.save()

            return HttpResponseRedirect('/employee/task')
    else:
        form = EmployeeTaskForm()
    return render(request, 'employee_task/add_task.html', {'form': form})


# TaskList
@login_required(login_url='/accounts/login')
def employeeTaskList(request):
    emp_task_list = EmployeeTasks.objects.all()
    print(emp_task_list)
    context = {'emp_task_list': emp_task_list}
    return render(request, 'employee_task/tasklist.html', context)


# Edit Task
@login_required(login_url='/accounts/login')
def task_edit(request, pk):
    task_id = int(pk)
    task = get_object_or_404(EmployeeTasks, pk=task_id)
    if request.method == "POST":
        form = EmployeeTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/employee/task')
    else:
        form = EmployeeTaskForm(instance=task)
    return render(request, 'employee_task/edit.html', {'form': form})


# Delete Task
@login_required(login_url='/accounts/login')
def task_delete(request, pk, template_name='employee_task/confirm_delete.html'):
    task = get_object_or_404(EmployeeTasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect("/employee/task")
    return render(request, template_name, {'object': task})
