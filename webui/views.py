from django.shortcuts import render

from main.models import Mails,Messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required





@login_required(login_url='login')
def index(request):
    return render(request,'index.html')
     

def login_view(request):
    if request.method =='POST':
        
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

        print(email,password)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request,'signin.html')
    

def logout_view(request):
    logout(request)