from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class student(models.Model):

    name = models.TextField(max_length=30)
    rollno = models.TextField(max_length = 30, default='DefaultRollNo')
    enrlno = models.TextField(max_length=20)
    course = models.TextField(max_length=30)
    phone = models.TextField(max_length=15)
    email = models.TextField(max_length=50)
    linkedin = models.TextField(max_length=100)
    skills = models.TextField(max_length = 500)
    image = models.ImageField(upload_to="upload/")
    


class placed_students(models.Model):
   company = models.TextField('50')
   batch = models.TextField(max_length='50')
   image = models.ImageField(upload_to="media") 
   name = models.TextField(max_length=30)
   phone = models.TextField(max_length=15)
   email = models.TextField(max_length=50)
   linkedin = models.TextField(max_length=100)