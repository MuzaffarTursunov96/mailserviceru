from django import forms
from main.models import Mails,Messages
from django.contrib.admin import widgets




class MailForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
  class Meta:
    model =Mails
    fields =['start_date','text_approval','fil_code_teg','end_date']

  