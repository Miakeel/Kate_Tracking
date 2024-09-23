from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
from .models import Participant
from django.forms import TextInput, EmailInput, NumberInput


import asyncio

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class EntryForm(forms.Form):
    qrcode_uuid = forms.UUIDField(widget=TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Scan Participant ID"
                }))
    

class QrcodeEditForm(forms.Form):
    qrcode_uuid = forms.UUIDField()

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('first_name', 'last_name', 'institution','email','title','phone','city','country','scfhs_number','participant_id')
        widgets = {
            "first_name": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "First Name"
                }),
            "last_name": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Last Name"
                }),
            "institution": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Institution"
                }),
            "title": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Title"
                }),
            "city": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "City"
                }),
            "country": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Country"
                }),
            "scfhs_number": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "SCFHS Number"
                }),
            "email": EmailInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Email"
                }),
            "phone": TextInput(attrs={
                'class':"form-control",
                'style':"max-width:300px;",
                'placeholder': "Phone"
                }),

            
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update(autofocus='autofocus')