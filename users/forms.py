from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(
        max_length=120, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'})
    )
    lastname = forms.CharField(
        max_length=120, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'})
    )

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'username', 'password1', 'password2']
# To add widgets for Existing fields like username , password1 and password2
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Setting custom labels
        self.fields['firstname'].label = 'First Name'
        self.fields['lastname'].label = 'Last Name'
        self.fields['email'].label = 'Email Address'
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        
        # Setting placeholders and classes
        self.fields['firstname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter First Name'
        })
        self.fields['lastname'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Last Name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Email Address'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
