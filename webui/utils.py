
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes





def send_verification_email(request,user, mail_subject, email_template):
  from_email =settings.DEFAULT_FROM_EMAIL
  current_site = get_current_site(request).domain
  # print(current_site)
  message =render_to_string(email_template,{
    'user':user,
    'domain':current_site,
    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
    'token':default_token_generator.make_token(user)
  })
  to_email = user.email
  email = EmailMessage(mail_subject,message,to=[to_email])
  email.content_subtype='html'
  email.send()