from django import forms
from main.models import Mails,Messages
from django.contrib.admin import widgets




class MailForm(forms.ModelForm):
  start_time = forms.DateField(widget=widgets.AdminTimeWidget)
  end_time = forms.DateField(widget=widgets.AdminTimeWidget)
  class Meta:
    model =Mails
    fields =['start_date','text_approval','fil_code_teg','end_date']

  