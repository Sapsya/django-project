from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from . models import Signup
class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)  
    class Meta():
        model=Signup
        fields='__all__'
class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)  
    class Meta():
        model=Signup
        fields=('Email','Password')
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Signup
        fields=('Name','Place','Age','Email',)
class ChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8)  
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8)  
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8)  
   
    
        
        
        
        