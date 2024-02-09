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

    student_list = student.objects.filter(course='MCA')

    for student_obj in student_list:
        student_obj.skills = student_obj.skills.split(' ')

    return render(request, 'mca.html', {'list': student_list})



def cyber(request):
    student_list = student.objects.filter(course='Cyber_Security')


    for student_obj in student_list:
        student_obj.skills = student_obj.skills.split(' ')

    return render(request, 'cyber.html', {'list': student_list})

def profile(request):
    
    student_list = student.objects.all()

    for student_obj in student_list:
        student_obj.skills = student_obj.skills.split(' ')

    return render(request, 'profile.html', {'list': student_list})

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
     if request.method=='POST':
         st = student()
         st.name = request.POST.get('name')
         st.course = request.POST.get('course')
         st.rollno = request.POST.get('rollno')
         st.enrlno = request.POST.get('enrlno')
         st.image = request.POST.get('image')
         st.email = request.POST.get('email')
         st.phone = request.POST.get('phone')
         st.linkedin = request.POST.get('linkedin')
         st.skills = request.POST.get('skills')

         st.save()
         return redirect('mca')
     return render(request, 'studentform.html')



