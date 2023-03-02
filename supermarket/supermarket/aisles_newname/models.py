from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 200)

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 200)

