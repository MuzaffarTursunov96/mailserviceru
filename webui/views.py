from django.shortcuts import render

from main.models import Mails,Messages
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
import uuid
from django.contrib.auth.decorators import login_required
from datetime import datetime
import datetime as ddate
from main.serializers import MailSerializer
from accounts.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .utils import send_verification_email
from accounts.models import Customer
from .forms import MailForm,MessageForm,CustomerForm
from django.contrib import messages




@login_required(login_url='login')
def index(request):
  yesterday = ddate.date.today() - ddate.timedelta(days=1)
  today_start=ddate.date.today() + ddate.timedelta(days=1)
  todays_mails_active = Mails.objects.filter(start_date__gt=yesterday,end_date__lt=today_start,used=False)
  todays_mails_used = Mails.objects.filter(start_date__gt=yesterday,end_date__lt=today_start,used=True)
  mails = Mails.objects.all()
  total_sent_mails =Mails.objects.filter(used=True).count()
  all_mail =mails.count()
  count_today =todays_mails_active.count() + todays_mails_used.count()
  # mailserializer = MailSerializer(mails,many=True)
  customers =Customer.objects.all()
  messages =Messages.objects.all()

  context ={
      'today_active':todays_mails_active,
      'today_used':todays_mails_used,
      'today_count':count_today,
      'mails':mails,
      'all_mail':all_mail,
      'total_sent_mails':total_sent_mails,
      'customer':customers,
      'messages':messages
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
    return redirect('login')

def forgot_password(request):
  if request.method == 'POST':
    email = request.POST.get('email',None)
    if email:
      if User.objects.filter(email=email).exists():
        user = User.objects.get(email__exact=email)
        #send the reset password email
        mail_subject='Reset your password'
        email_template='accounts/emails/reset_password_email.html'
        send_verification_email(request, user, mail_subject, email_template)

        # messages.success(request,'Passoword reset link has been sent to your email addres.')
        return redirect('login')
      else:
        # messages.error(request,'Account does not exist.')
        return redirect('forgot_password')
    else:
    #   messages.error(request,'Email incorrect')
      return redirect('forgot_password')
  return render(request,'accounts/forgot_password.html')


def reset_password_validate(request, uidb64, token):
  try:
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User._default_manager.get(pk=uid)
  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None
  
  if user is not None and default_token_generator.check_token(user,token):
    request.session['uid']=uid
    # messages.info(request,'Please reset your password')
    return redirect('reset_password')
  else:
    # messages.error(request,'This link has been expired')
    return redirect('index')



def reset_password(request):
  if request.method == "POST":
    password = request.POST.get('password',None)
    confirm_password = request.POST.get('confirm_password',None)

    if password == confirm_password and password is not None:
      pk = request.session.get('uid')
      user =User.objects.get(pk=pk)
      user.set_password(password)
      user.is_active =True
      user.save()
    #   messages.success(request,'Password reset successfully!')
      return redirect('login')
      
    else:
    #   messages.error(request,"Password don't match")
      return redirect('reset_password')

  return render(request,'accounts/reset_password.html')


def singup(request):
    if request.method =='POST':
        pass
   

    return render(request,'signup.html')


def elements(requests):
  return render(requests,'element.html')

def widgets(requests):
  return render(requests,'widget.html')

def forms(requests):
  return render(requests,'form.html')

def tables(requests):
  return render(requests,'table.html')

def charts(requests):
  return render(requests,'chart.html')



def not_found(requests):
  return render(requests,'404.html')

def button(requests):
  return render(requests,'button.html')

def blank(requests):
  return render(requests,'blank.html')

def typography(requests):
  return render(requests,'typography.html')





def add_mail(request):
  return render(request,'elements/add_mail.html')

def add_message(request):
  return render(request,'elements/add_message.html')

def add_customer(request):
  return render(request,'elements/add_customer.html')



# Details

def customer_detail(request,pk):
  customer =  get_object_or_404(Customer,pk=pk)
  if request.method =='POST':
    data =request.POST
    form =CustomerForm(data=data,instance =customer)
    if form.is_valid():
      form.save()
    else:
      messages.error(request, form.errors)
  form =CustomerForm(instance =customer)
  context ={
    'customer':customer
  }
  return render(request,'detail/customer_detail.html',context)
  
def message_detail(request,pk):
  message =  get_object_or_404(Messages,pk=pk)
  if request.method =='POST':
    data =request.POST
    form =MessageForm(data=data,instance =message)
    if form.is_valid():
      form.save()
    else:
      messages.error(request, form.errors)
  form =MessageForm(instance =message)
  context ={
    'message':message,
    'form':form

  }
  return render(request,'detail/message_detail.html',context)


def mail_detail(request,pk):
  mail =  get_object_or_404(Mails,pk=pk)
  if request.method =='POST':
    data =request.POST
    form =MailForm(data=data,instance =mail)
    if form.is_valid():
      form.save()
    else:
      messages.error(request, form.errors)
  
  form = MailForm(instance=mail)
  context ={
    'mail':mail,
    'form':form
  }
  return render(request,'detail/mail_detail.html',context)


# list
def mail_list(request):
  return render(request,'list/mail_list.html')

def customer_list(request):
  return render(request,'list/customer_list.html')


def message_list(request):
  return render(request,'list/message_list.html')
  





