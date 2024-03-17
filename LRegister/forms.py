from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'name': 'pswd1', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'name': 'pswd2', 'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={
                'name': 'txt',
                'placeholder': 'User Name'
            }),
            'email' : forms.EmailInput(attrs={
                'name': 'email',
                'placeholder': 'Email',
            }),
        }
