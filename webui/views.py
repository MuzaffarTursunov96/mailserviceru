from django.shortcuts import render

from main.models import Mails,Messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required





@login_required(login_url='login')
def index(request):
    return render(request,'index.html')
     

def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
    else:
        redirect('login')
    

def logout_view(request):
    logout(request)