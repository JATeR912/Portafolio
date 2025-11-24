from django import forms
from .models import Proyecto, Habilidad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'experiencia']


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'titulo',
            'descripcion',
            'imagen',
            'demo_url',
            'repo_url',
            'habilidades'
        ]
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']