from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.filme.models import Usuario


class FormHomepage(forms.Form):
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')
