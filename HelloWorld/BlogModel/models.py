from django.db import models

class Blog(models.Model):
    categoryId = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    authorId = models.CharField(max_length=20)
    remark = models.CharField(max_length=100)
