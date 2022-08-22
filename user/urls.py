from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('facebookLogin',facebookLogin,name="facebookLogin"),
    path('logoutProcess/',logoutProcess,name="logoutProcess"),
    path('profileForm/',profileForm,name="profileForm"),
    path("editProfile/",editProfile,name="editProfile")

] 