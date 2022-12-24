from django import forms
from main.models import Mails,Messages
from django.contrib.admin import widgets
from accounts.models import Customer
from django.forms import widgets
from datetime import datetime
from main.utils import split_filter_text
import pytz
timezones = pytz.all_timezones


class MailForm(forms.ModelForm):
  start_date =forms.DateField(
        initial=datetime.now().strftime("%Y-%m-%d %H:%M"),
        widget=forms.widgets.DateInput(
            attrs={'type': 'date'})
    )
  end_date =forms.DateField(
        initial=datetime.now().strftime("%Y-%m-%d %H:%M"),
        widget=forms.widgets.DateInput(
            attrs={'type': 'date'})
    )
  def clean(self):
    cleaned_data = super(MailForm, self).clean()
    end_date = cleaned_data['end_date']
    start_date = cleaned_data['start_date']
    # do your cleaning here
    if start_date > end_date:
      raise forms.ValidationError("Start date should be before end date.")


    d1 =cleaned_data['end_date'].strftime("%Y-%m-%d %H:%M")
    d2 =datetime.now().strftime("%Y-%m-%d %H:%M")

    if d1 <= d2:
        raise forms.ValidationError("end_date can't be little now!")

    text_number =split_filter_text(cleaned_data['fil_code_teg'])

    if len(text_number['number_list']) < 1:
        raise forms.ValidationError(" Phone code can't be null, you must enter. For example fil_code_teg entering like this: '78941,text1,23365,78894,text2' ")
    
    if len(text_number['text_list']) < 1:
        raise forms.ValidationError(" Tag can't be null, you must enter. For example fil_code_teg entering like this: 'text1,78941,334444,text2,78894' ")

    
    return cleaned_data

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
  created_date_to_send =forms.DateField(widget=widgets.SelectDateWidget)
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

  def clean(self):
    cleaned_data = super(MessageForm, self).clean()
    if cleaned_data['status'] not in ['processing','message_sent','to_be_sent']:
            raise forms.ValidationError({"status": "status must select from this list ['processing','message_sent','to_be_sent'] "})
    return cleaned_data



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
  def clean(self):
    cleaned_data = super(CustomerForm, self).clean()

    phone_number =cleaned_data['phone_number']
    for val in phone_number:
      if val not in "0123456789":
          raise forms.ValidationError('You must add phone number like this 74951234567 ')

    if phone_number[0]!='7':
        raise forms.ValidationError('First letter should be "7"')

    phone_code =cleaned_data['phone_code']
    for val in phone_code:
      if val not in "+1234567890()":
          raise forms.ValidationError('You must add phone number like this +7 (495) or 39022')
    timezone =cleaned_data['timezone']
    if timezone not in timezones:
      raise forms.ValidationError(f'You must select from this links "{timezones}"')
    return cleaned_data
  
  class Meta:
    model =Customer
    fields =['phone_number','phone_code','teg','timezone']

  