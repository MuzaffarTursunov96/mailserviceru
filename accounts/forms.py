from django import forms
from .models import UserProfile,User


class ProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control bg-dark'
            })
  class Meta:
    model =UserProfile
    fields ="__all__"

class UserForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control bg-dark'
            })
  class Meta:
    model =User
    fields =["first_name",'last_name','username','email','phone_number']


