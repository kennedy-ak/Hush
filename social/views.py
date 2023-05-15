from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "social/index.html")


def login(request):
    return render(request, "registration/login.html")

def signup(request):
        
        
        
        if request.method == "POST":
    

            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['password1']

            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email Taken")
                    redirect('signup')

                elif User.objects.filter(username= username).exists():
                    messages.info(request, "Username Taken")
                    redirect('signup')

                else:
                    user = User.objects.create_user(username=username,email=email,password=password1)
                    user.save()
                    return redirect('home')
            else:           
                messages.info(request, 'Password Not Matching')
                return redirect('signup')
        else:     
            return render(request, "registration/signup.html")
        



