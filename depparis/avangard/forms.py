from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
#from captcha.fields import CaptchaField

from .models import *


class RegisterUserForm(UserCreationForm):
        error_messages = {
                "password_mismatch": "The two password fields didn't match"
        }
        username = forms.CharField(
                label = 'Nom',
                widget = forms.TextInput(
                        attrs = {'class': 'form-input'}
                )
        )
        phone = forms.CharField(
                label = 'Numero de telephone',
                widget = forms.TextInput(
                        attrs = {'class': 'form-input'}
                )
        )
        email = forms.EmailField(
                label = 'E-mail',
                widget = forms.EmailInput(
                        attrs = {'class': 'form-input'}
                )
        )
        password1 = forms.CharField(
                label = "Mot de passe",
                widget = forms.PasswordInput(),
                help_text = password_validation.password_validators_help_text_html()
        )
        password2 = forms.CharField(
                label = "Mot de passe confirmer",
                widget = forms.PasswordInput(),
                help_text = "Enter the same password as before, for verification"
        )
        #captcha = CaptchaField()

        class Meta:
                model = Personal
                fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
        username = forms.CharField(label = 'Connexion', widget = forms.TextInput(attrs = {'class': 'form-input'}))
        password = forms.CharField(label = 'Mot de passe',
                                   widget = forms.PasswordInput(attrs = {'class': 'form-input'}))
        #captcha = CaptchaField()


class ContactForm(forms.Form):
        name = forms.CharField(label = 'Nom', max_length = 255)
        email = forms.EmailField(label = 'Email')
        phone = forms.CharField(label = 'Numero de telephone', max_length = 255)
        theme = forms.CharField(label = 'Theme', max_length = 255)
        message = forms.CharField(label = 'Votre message', widget = forms.Textarea(attrs = {'cols': 60, 'rows': 10}))
        inviter_maitre = forms.CharField(label = 'Numero de telephone', max_length = 255)
