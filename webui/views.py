from django.shortcuts import render

from main.models import Mails,Messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from datetime import datetime
from main.serializers import MailSerializer





@login_required(login_url='login')
def index(request):
    todays_mails_active = Mails.objects.filter(start_date__lte=datetime.now(),end_date__gte=datetime.now(),used=False)
    todays_mails_used = Mails.objects.filter(start_date__lte=datetime.now(),end_date__gte=datetime.now(),used=True)
    mails = Mails.objects.all()
    all =mails.count()
    count_today =todays_mails_active.count() + todays_mails_used.count()
    mailserializer = MailSerializer(mails,many=True)

    context ={
        'today_active':todays_mails_active,
        'today_used':todays_mails_used,
        'today_count':count_today,
        'mails':mailserializer.data,
        'all':all
    }
    return render(request,'index.html',context)
     

def login_view(request):
    if request.method =='POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)

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