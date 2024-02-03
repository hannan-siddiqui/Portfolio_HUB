from django.contrib import admin

from django.contrib import admin
from .models import *
from theportfolio import *



class studentdata(admin.ModelAdmin):
    list_display = ("rollno","course", "enrlno", "image", "name", "phone", "email", "linkedin", "skills")

class placeddata(admin.ModelAdmin):
    list_display = ("company", "batch", "image", "name", "linkedin")

admin.site.register(student, studentdata)
admin.site.register(placed_students, placeddata)