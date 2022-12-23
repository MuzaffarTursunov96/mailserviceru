from django import forms
from main.models import Mails,Messages
from django.contrib.admin import widgets
from accounts.models import Customer



class MailForm(forms.ModelForm):
  start_date =forms.DateField(widget=widgets.AdminDateWidget)
  end_date =forms.DateField(widget=widgets.AdminDateWidget)
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            # if field =='start_date' or field =='end_date':
            #    self.fields[field].widget.attrs.update({
            #     'class': 'datepicker'
            # })
  class Meta:
    model =Mails
    fields =['start_date','text_approval','fil_code_teg','end_date']


class MessageForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
  class Meta:
    model =Messages
    fields =['created_date_to_send','status','mail','customer']

class CustomerForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
  class Meta:
    model =Customer
    fields =['phone_number','phone_code','teg','timezone']

  