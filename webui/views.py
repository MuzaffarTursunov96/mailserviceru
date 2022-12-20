from django.shortcuts import render

from main.models import Mails,Messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
import uuid
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .utils import send_verification_email





@login_required(login_url='login')
def index(request):
    return render(request,'index.html')
     

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



