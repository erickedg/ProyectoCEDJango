from django.db import models
 
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    grade = models.CharField(max_length=50)