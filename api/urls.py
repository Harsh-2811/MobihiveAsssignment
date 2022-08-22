from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('authenticate/',MyTokenObtainPairView.as_view(),name="authenticate"),
    path("getUserInformation/<str:SecureCode>/",getUserInformation.as_view(),name="getUserInformation")

] 