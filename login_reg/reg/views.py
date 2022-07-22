from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def Sign_up(request):
    if request.method == 'POST':
        fm= SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render (request, 'reg/signup.html',{'form':fm})


#Login View
def User_login(request):
    if  not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'reg/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/prof/')




def User_profile(request):
    if request.user.is_authenticated:
        return render(request, 'reg/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

