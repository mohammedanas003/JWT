from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    ph_no=models.CharField(max_length=10)
    def __str__(self):
        return self.username
    

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)

