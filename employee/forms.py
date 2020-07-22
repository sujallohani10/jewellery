from django import forms
from .models import EmployeeTasks, Employee


class EmployeeTaskForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    description = forms.CharField(widget=forms.Textarea, label='Description')

    class Meta:
        model = EmployeeTasks
        fields = ('employee', 'item', 'image', 'description', 'gold_weight', 'silver_weight', 'bronze_weight',
                  'given_date', 'completion_date', )
