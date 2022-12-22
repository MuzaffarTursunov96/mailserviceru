from django import forms
from main.models import Mails,Messages
from MinimalSplitDateTimeMultiWidget import MinimalSplitDateTimeMultiWidget
from django.forms import DateTimeField




class MailForm(forms.ModelForm):
  class Meta:
    model =Mails
    fields =['start_date','text_approval','fil_code_teg','end_date']

  start_date = DateTimeField(widget=MinimalSplitDateTimeMultiWidget())
  end_date = DateTimeField(widget=MinimalSplitDateTimeMultiWidget())