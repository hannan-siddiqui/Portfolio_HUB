from django.db import models


class student(models.Model):

    name = models.TextField(max_length=30, null=True)
    rollno = models.TextField(max_length = 30, default='22CAMSA420')
    enrlno = models.TextField(max_length=20,null=True)
    course = models.TextField(max_length=30, default='MCA', null=True)
    phone = models.TextField(max_length=15, null=True) 
    email = models.TextField(max_length=50, null=True)
    linkedin = models.TextField(max_length=100, null=True)
    skills = models.TextField(max_length = 500, null=True)
    image = models.ImageField(upload_to="upload/", null=True)
    


class placed_students(models.Model):
   company = models.TextField('50')
   batch = models.TextField(max_length='50')
   image = models.ImageField(upload_to="media") 
   name = models.TextField(max_length=30)
   linkedin = models.TextField(max_length=100)