from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=25)
    Place=models.CharField(max_length=25)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Age=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
