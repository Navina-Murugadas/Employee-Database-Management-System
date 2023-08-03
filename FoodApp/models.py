from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_ID = models.IntegerField()
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Gender = models.CharField(max_length=10)
    Date_of_Birth = models.DateField()
    Mobile_No =  models.CharField(max_length=10)
    Organization = models.CharField(max_length=20)
    Date_of_join = models.DateField()
    Salary = models.CharField(max_length=10)
    Email = models.EmailField(max_length=30)
    Address = models.CharField(max_length=100)
    Vaccine_status = models.BooleanField()
    Display_picture = models.ImageField(upload_to='pics', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.First_Name



