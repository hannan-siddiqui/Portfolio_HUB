
from django import views
from django.contrib import admin
from django.urls import path
from theportfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutpage, name= 'logoutpage'),
    path('login/', views.loginpage, name = 'loginpage'),
    path('register/', views.register, name = 'register'),
    path("", views.mca, name = 'mca'),
    # path('mca/', views.mca, name = 'mca'),
    path("csdf/", views.cyber, name = 'cyber'),
    path('studentform/', views.studentform, name='studentform'),
    
]
