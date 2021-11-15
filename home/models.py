from django.db import models
# Create your models here.

        

class Employer(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=False,
    error_messages={'unique':"user already exist",})
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    role = models.CharField(max_length=10, default='Employer')


    def __str__(self):
        return self.email
    
class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=False,
    error_messages={'unique':"user already exist",})
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    role = models.CharField(max_length=10, default='Employee')


    def __str__(self):
        return self.email