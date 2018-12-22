from django.db import models

class User(models.Model):
	number = models.CharField(max_length=32)
	password= models.CharField(max_length=32)