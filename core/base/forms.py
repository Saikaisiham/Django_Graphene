from django import forms
import json
from .models import SettingUser,User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.Form):

    


    

    class Meta :
        model = SettingUser
        fields = ['first_name','last_name','email','city','avatar','current_address','CIN']




class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
