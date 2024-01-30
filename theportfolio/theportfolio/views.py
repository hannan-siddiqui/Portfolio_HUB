from audioop import reverse
from django.contrib.auth import authenticate, login, logout
from MySQLdb import IntegrityError
from django.http import HttpResponseRedirect
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



def loginpage(request):
    if request.method == "POST":
        # Attempt to sign user in
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return  redirect('mca')
        else:
            return redirect('loginpage')
    else:
        return render(request, "login.html")

def logoutpage(request):
    logout(request)
    return redirect('mca')

def register(request):
    if request.method == "post":
        enrlno = request.POST.get('your enrollment no. ')
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        # if enrlno not in enrlnolist:
        #     return redirect('mca')


        try:
            user = User.objects.create_user(enrlno, email, pass1)
            user.save()
        except IntegrityError:
            return redirect('register')
        login(request, user)
        return HttpResponseRedirect(reverse("mca"))
    else:
        return render(request, "register.html")







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



