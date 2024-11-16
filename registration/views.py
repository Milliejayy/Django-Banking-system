from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import FormData #We import the class of the form we created in our forms.py
from . models import UserForm

# Create your views here.

def index(request):
    user_items = UserForm.objects.all()

    return render(request, "registration/index.html", {
        "user_items": user_items
    })


def register(request):
    register = FormData()

    if request.method == "POST" :
        register = FormData(request.POST)
        if register.is_valid() :
            register.save() 
            return redirect("index")
        


        else:
            messages.error(request, "This email is already registered!")
            return render(request, "registration/register.html",{"form":register})
        
    return render(request, "registration/register.html",{"form":register})


def user_login(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        password = request.POST["password"]
        user = authenticate(request, firstname=firstname, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "Login successful!")
            return redirect("registration:index")
        else:
            #messages.error(request, "Your firstname or password is incorrect. Please try again!")
            return redirect("registration:login")
        
    return render(request, "registration/login.html",{})

def user_logout(request):

    #logout(request)
    return render(request, 'registration/logout.html') 




