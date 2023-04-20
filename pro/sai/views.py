from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login
import re

# from .models import CustomUser

def home1(request):
    return render(request,"home1.html")



#view for signup module
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        createpassword = request.POST.get('createpassword')
        confirmpassword = request.POST.get('confirmpassword')
        #if createpassword!=confirmpassword:
           # return redirect('signup')
        username_regex = r'^[a-zA-Z0-9_-]{4,}$'
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z\d\W]{8,}$'
        if User.objects.filter(email=email).exists():

           # return redirect('signup')
            return render(request, 'signup.html', {'error_message': 'Invalid input'})

        username_valid = re.match(username_regex, username)
        password_valid = re.match(password_regex, createpassword)
        if username_valid and password_valid and createpassword == confirmpassword:
            #  salt = bcrypt.gensalt()
            # hashed_password = bcrypt.hashpw(createpassword.encode())
            my_user = User.objects.create_user(username,email,createpassword)
            my_user .save()
            return redirect('login')
 
    return render(request, 'signup.html') 



def login(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        createpassword=request.POST.get('createpassword')
        user=authenticate(request,username=username,password=createpassword)
        if user is not None:
            auth_login(request, user)
            return redirect('home1')
        else:
            return redirect('login')
    else:
        return render(request,"login.html")

  
# def secondsign(request):
#     if request.method=='POST':

#     return render(request,'home1.html')


     



