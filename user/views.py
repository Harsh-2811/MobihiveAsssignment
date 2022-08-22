from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import QrCode
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

@login_required(login_url='facebookLogin')
def home(request):
    if not request.user.phone_number:
        return redirect("profileForm")
    return render(request,'index.html')

def facebookLogin(request):
    return render(request,'login.html')

@login_required(login_url='facebookLogin')
def logoutProcess(request):
    logout(request)
    return redirect('facebookLogin')

@login_required(login_url='facebookLogin')
def profileForm(request):
    if request.method == "POST":
        phone_number = request.POST['phonenumber']
        city = request.POST['city']
        address = request.POST['address']
        secureCode = request.POST['code']
        
        request.user.phone_number = phone_number
        request.user.city = city
        request.user.address = address
        request.user.SecureCode=secureCode
        request.user.save()
        QrCode.objects.create(user = request.user)
        return redirect('home')

    return render(request,"profileForm.html")

@login_required(login_url='facebookLogin')
def editProfile(request):
    if request.method == "POST":
        phone_number = request.POST['phonenumber']
        city = request.POST['city']
        address = request.POST['address']
        secureCode = request.POST['code']
        request.user.phone_number = phone_number
        request.user.city = city
        request.user.address = address
        request.user.SecureCode=secureCode
        request.user.save()
        request.user.qrcode.save()
        return redirect('home')

    return render(request,"profileForm.html")