from django.db import models

class ResourceClass(models.Model):
	name = models.CharField(max_length=20)
	item = models.CharField(max_length=20)
	remark = models.CharField(max_length=40)
