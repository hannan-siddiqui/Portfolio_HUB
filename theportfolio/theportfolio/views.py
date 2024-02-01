from audioop import reverse
from django.contrib.auth import authenticate, login, logout
from MySQLdb import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from APP.models import *
from theportfolio import*

from django.contrib.auth.models import User


enrlnolist = ['gl6182', 'gl6100']


def mca(request):

    studentlist = {
        "list" : student.objects.all(),
    }

    return render(request, 'mca.html', studentlist)



def cyber(request):
    return render(request, 'cyber.html')



def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            try:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('loginpage')
            except: IntegrityError
            return redirect('register')

            return redirect('loginpage')
        

    return render (request,'register.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('mca')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('mca')


def studentform(request):
     if request.method=='post':
         student = student()
         student.course = request.post['course']
         student.enrlno = request.post['enrlno']
         student.image = request.post['iamge']
         student.name = request.post['name']
         student.phone = request.post['email']
         student.linkedin = request.post['linkedin']
         student.skills = request.post['skills']
         student.save()
         return redirect('mca')
     return render(request, 'studentform.html')



def profile(request):
    return render(request, 'profile.html')



