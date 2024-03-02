from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from theportfolio import views
from django.conf.urls.static import static
from django.conf import settings
from media import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutpage, name= 'logoutpage'),
    path('login/', views.loginpage, name = 'loginpage'),
    path('register/', views.register, name = 'register'),
    path("mca/", views.mca, name = 'mca'),
    path('student/<int:stid>/', views.viewmore, name='viewmore'),
    path("csdf/", views.cyber, name = 'cyber'),
    path('studentform', views.studentform, name='studentform'),

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)