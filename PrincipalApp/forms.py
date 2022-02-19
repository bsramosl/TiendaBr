from builtins import property
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, Form, Select
from .models import *

class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=140, required=False,widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}))
    first_name = forms.CharField(max_length=140, required=True,widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=140, required=False,widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = (
            'username', 
            'password'
        )


class RegistroProducto(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'input'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Descripcionrio','class': 'input'}))
    precio = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Precio','class': 'input'}))    
    class Meta:
        model = Producto
        fields = '__all__'


class RegistroCategoria(forms.ModelForm): 
    class Meta:
        model = Producto
        fields = '__all__'
