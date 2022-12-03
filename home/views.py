from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# password : kanha$2012
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has enetered correct Credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # A backend authenticated the credentials
            return redirect('/')
        else:
            # No backend authenticated the credentials    
            return render(request,'login.html')
    return render(request,'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('/login')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        signup = Customer(name=name, email=email, phone=phone, age=age, date=datetime.today())
        signup.save()
        messages.success(request, 'Customer Registered successfully')
    return render(request,'signup.html')