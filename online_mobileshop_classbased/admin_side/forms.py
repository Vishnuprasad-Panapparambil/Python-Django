from django.forms import ModelForm
from .models import Brand,Mobile
from django import forms
from customer.models import Orders

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brand
        fields='__all__'
        widgets={
            'brand_name':forms.TextInput(attrs={'class':'form-control'})
        }

class MobileCreateFrm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
        widgets={
            "mobile_name" :forms.TextInput(attrs={'class':'form-control'}),

            "ram" :forms.TextInput(attrs={'class':'form-control'}),
            "storage" :forms.TextInput(attrs={'class': 'form-control'}),

            "camera" :forms.TextInput(attrs={'class':'form-control'}),
            "os" :forms.TextInput(attrs={'class':'form-control'}),
            "price" :forms.TextInput(attrs={'class':'form-control'}),
            "cart_status":forms.HiddenInput(),

        }

class OrderupdateFrm(ModelForm):
    class Meta:
        model=Orders
        fields=['personname','address','email','status']
        widgets={
            "personname" :forms.TextInput(attrs={'class':'form-control'}),

            "address" :forms.TextInput(attrs={'class':'form-control'}),

            "email": forms.TextInput(attrs={'class': 'form-control'}),
        }


