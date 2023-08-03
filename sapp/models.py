from django.db import models

# Create your models here.
class Book(models.Model):
    bookname = models.CharField(max_length=100)
    authur = models.CharField(max_length=100)
    publisher = models.CharField(max_length=20)
    price = models.IntegerField(max_length=20)