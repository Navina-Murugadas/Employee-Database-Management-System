from django.shortcuts import render, redirect
from FoodApp.models import Employee
from FoodApp.forms import EmployeeForm
from FoodApp.forms import UpdateForm
import datetime

# Create your views here.
def welcome(request):
    dt = datetime.datetime.now()
    hour = int(dt.strftime('%H'))
    if (hour>=6 and hour<12):
        msg = 'Good Morning!!!'
    elif (hour>=12 and hour<16):
        msg = 'Good Afternoon!!!'
    elif (hour>=16 and hour<19):
        msg = 'Good Evening!!!'
    else:
        msg = 'Bonjour!!!'

    dt_dict = {'Datetime':dt, 'Greet':msg}
    return render(request, 'FoodApp/food.html', context=dt_dict)

def retrieve(request):
    employee = Employee.objects.all()
    return render(request, 'FoodApp/index.html', {'employee':employee})

def create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/food/show/')
    else:
        form = EmployeeForm()
    return render(request, 'FoodApp/create.html', {'form':form})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/food/show/')

def update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=employee)
        if form.is_valid:
            form.save()
            return redirect('/food/show/')
    return render(request, 'FoodApp/update.html', {'employee':employee})

def thank(request):
    return render(request, 'FoodApp/thanks.html')

