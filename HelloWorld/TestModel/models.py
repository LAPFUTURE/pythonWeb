from django.db import models
# models.py
from django.db import models
 
class Test(models.Model):
    number = models.CharField(max_length=20)
    password= models.CharField(max_length=20)
# Create your models here.

