from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    salary = models.FloatField(default=1200)
    phone = models.PositiveIntegerField(unique=True)
    birth_date = models.DateField
    charge = models.CharField(max_length=100)

