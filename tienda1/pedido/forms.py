from django import forms
from django.forms import ModelForm
from pedido.models import Articulos

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioArticulo(ModelForm):
    
    nombre= forms.CharField(min_length=2, max_length=160)
    
    class Meta:
        model = Articulos
        fields = '__all__'

class CustomUserForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']