import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Food_Django.settings')

import django
django.setup()

from FoodApp.models import *
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fEmp_ID = faker.iana_id()
        fFirst_Name = faker.first_name()
        fLast_Name = faker.last_name()
        fGender = faker.random_element(['Male','Female'])
        fDate_of_Birth = faker.date_of_birth()
        fMobile_No = randint(6010010010, 9999999999)
        fOrganization = faker.random_element(['Swiggy', 'Zomato', 'Dunzo', 'UberEats', 'FoodPanda', 'Dominos', 'PizzaHut', 'KFC'])
        fDate_of_join = faker.date_this_year()
        fSalary = randint(20000, 120000)
        fEmail = faker.email()
        fAddress = faker.address()
        fVaccine_status = faker.boolean(chance_of_getting_true=75)

        emp_record = Employee.objects.get_or_create(Emp_ID=fEmp_ID, First_Name=fFirst_Name, Last_Name=fLast_Name, Gender=fGender, Date_of_Birth=fDate_of_Birth, Mobile_No=fMobile_No, Organization=fOrganization, Date_of_join=fDate_of_join, Salary=fSalary, Email=fEmail, Address=fAddress, Vaccine_status=fVaccine_status)

generate(20)

