
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from decouple import config
import requests as rq



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


def send_message(messages):
    all_aproved =True
    for message in messages:
        data_object = {
            "id": message.customer.id,
            "phone": message.customer.phone_number,
            "text": message.mail.text_approval
        }
        token =config("TOKEN")
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        api_link = "https://probe.fbrq.cloud/v1/send/{a}".format(a=message.id)
        output = rq.post(api_link, headers=headers,json=data_object)

        if output.status_code == 200:
            message.status ='message_sent'
            message.save()
        else:
            all_aproved=False

    return all_aproved


def send_message_single(message):
    all_aproved =True
    data_object = {
        "id": message.customer.id,
        "phone": message.customer.phone_number,
        "text": message.mail.text_approval
    }
    token =config("TOKEN")
    headers={
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    api_link = "https://probe.fbrq.cloud/v1/send/{a}".format(a=message.id)
    output = rq.post(api_link, headers=headers,json=data_object)

    if output.status_code == 200:
        message.status ='message_sent'
        message.save()
    else:
        all_aproved=False

    return all_aproved