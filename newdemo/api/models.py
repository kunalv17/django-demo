from django.db import models


class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70, unique=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    description=models.TextField(default=None)
    price=models.IntegerField()
    image=models.TextField(default=None)

    def __str__(self):
        return self.name
    
