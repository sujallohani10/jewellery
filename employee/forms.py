from django import forms


class EmployeeTaskForm(forms.Form):
    item = forms.CharField(max_length=100, label='Task Item')
    description = forms.CharField(widget=forms.Textarea, label='Description')
    gold_weight = forms.CharField(max_length=100, label='Gold Weight')
    silver_weight = forms.CharField(max_length=100, label='Silver weight')
    bronze_weight = forms.CharField(max_length=100, label='Bronze weight')
    task_given_date = forms.DateTimeField(label='Task Given Date')
    completion_date = forms.DateTimeField(label='Completion Date')
