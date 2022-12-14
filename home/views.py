from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from home.models import Customer
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm #denis
from .forms import CreateUserForm
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

def signup(request): #denis
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'signup.html',context)


    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     age = request.POST.get('age')
    #     password = request.POST.get('password')
    #     signup = Customer(name=name, email=email, phone=phone, age=age, password=password, date=datetime.today())
    #     signup.save()
    #     messages.success(request, 'Customer Registered successfully')


# for customer
# def loginCustomer(request):
#     if request.method=="POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         # username = User.objects.get(email=email).username
#         # check if user has enetered correct Credentials
#         customer = authenticate(email=email, password=password)
#         if customer is not None:
#             login(request,customer)
#             # A backend authenticated the credentials
#             return redirect('customer.html')
#         else:
#             # No backend authenticated the credentials    
#             return render(request,'customerLogin.html')
#     return render(request,'customerLogin.html')

# def logoutCustomer(request):
#     logout(request)
#     return redirect('/customerLogin')
