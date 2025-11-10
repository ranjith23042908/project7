from django.contrib.auth.models import User
from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=50)
    remarks=models.CharField(max_length=50)
    status=models.IntegerField()


class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    salary=models.FloatField()
    status=models.IntegerField()


class Email(models.Model):
    name=models.CharField(max_length=50,unique=True)
    age=models.IntegerField()
    email=models.EmailField(max_length=50,unique=True)

class Salary(models.Model):
    salary = models.FloatField()
    email= models.OneToOneField(Email,on_delete=models.CASCADE,null=True,db_column='email_id')

class Account(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50,unique=True)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class AuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)