from django import forms
from FoodApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('Emp_ID', 'First_Name', 'Last_Name', 'Gender', 'Date_of_Birth', 'Organization', 'Date_of_join', 'Email')