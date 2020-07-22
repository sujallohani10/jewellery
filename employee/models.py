from django.db import models


# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    contact_info = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_photo = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class EmployeeTasks(models.Model):
    employee = models.ForeignKey(Employee, default=1, verbose_name="Tasks", on_delete=models.SET_DEFAULT)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tasks/images/', blank=True)
    description = models.CharField(max_length=250)
    gold_weight = models.CharField(max_length=50)
    silver_weight = models.CharField(max_length=50)
    bronze_weight = models.CharField(max_length=50)
    given_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    completion_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # otherwise we get "Employee Tasks in admin"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.item
