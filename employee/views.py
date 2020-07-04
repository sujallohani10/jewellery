from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EmployeeTaskForm


def employeeTask(request):
    submitted = False
    if request.method == 'POST':
        form = EmployeeTaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = EmployeeTaskForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'employee/task.html', {'form': form, 'submitted': submitted})
