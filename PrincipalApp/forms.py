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


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Descripcionrio','class': 'form-control'}))
    precio = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': 'Precio','class': 'form-control'}))    
    foto =forms.FileField(label='Imagen',widget=forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}))
    foto1 =forms.FileField(label='Imagen',widget=forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}))
    foto2 =forms.FileField(label='Imagen',widget=forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}))
    foto3 =forms.FileField(label='Imagen',widget=forms.FileInput(attrs={'class':'form-control', 'id':'customFile'}))
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm): 
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Descripcionrio','class': 'form-control'}))
    class Meta:
        model = Categoria
        fields = '__all__'
 

class CarritoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'}))
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'}))
    cantidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control'}))
    class Meta:
        model = Carrito
        fields = '__all__'
