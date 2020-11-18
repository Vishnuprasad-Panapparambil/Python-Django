from django import forms
from django.forms import ModelForm
from .models import Orders,Cart
from admin_side.models import Mobile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(ModelForm):
    class Meta:
        model=Mobile
        fields = ['mobile_name','brand','price','os','camera']
        widgets={
            "mobile_name" :forms.TextInput(attrs={'class':'form-control'}),
            "camera" :forms.TextInput(attrs={'class':'form-control'}),
            "os" :forms.TextInput(attrs={'class':'form-control'}),
            "price" :forms.TextInput(attrs={'class':'form-control'}),
        }

class Orderform(ModelForm):
    class Meta:
        model=Orders
        fields = '__all__'
        widgets={
            "personname" :forms.TextInput(attrs={'class':'form-control'}),

            "address" :forms.TextInput(attrs={'class':'form-control'}),
            "pin" :forms.TextInput(attrs={'class':'form-control'}),
            "phone" :forms.TextInput(attrs={'class':'form-control'}),
            "email" :forms.TextInput(attrs={'class':'form-control'}),
            "productid": forms.TextInput(attrs={'readonly': 'readonly'}),

            "product_name" : forms.TextInput(attrs={'readonly': 'readonly'}),
            "status":forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "active_status":forms.HiddenInput(),

        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets={
            "username" :forms.TextInput(attrs={'class':'form-control'}),

            "email" :forms.TextInput(attrs={'class':'form-control'}),
            "password1" :forms.TextInput(attrs={'class':'form-control'}),
            "password2" :forms.TextInput(attrs={'class':'form-control'}),
        }

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields ='__all__'
        widgets={

            "productname": forms.HiddenInput(),

            "user": forms.HiddenInput(),
            "productid": forms.HiddenInput(),
            "cart_status": forms.HiddenInput(),

        }