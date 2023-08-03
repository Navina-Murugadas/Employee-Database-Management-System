from django.contrib import admin
from FoodApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    Emp_list = ['Emp_ID', 'First_Name', 'Last_Name', 'Gender', 'Date_of_Birth', 'Mobile_No', 'Organization', 'Date_of_join', 'Salary', 'Email', 'Address', 'Vaccine_status', 'Display_picture']

admin.site.register(Employee, EmployeeAdmin)
