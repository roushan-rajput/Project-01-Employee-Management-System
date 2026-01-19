from django.db import models

# Create your models here.
class employee(models.Model):
    empid=models.CharField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    position=models.CharField(max_length=50)
    salary=models.CharField()
    Password=models.CharField(max_length=6)

class passwordrest(models.Model):
    email=models.EmailField()
    classotp=models.CharField(max_length=6)

     
    