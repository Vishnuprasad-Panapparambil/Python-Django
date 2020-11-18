from django.forms import ModelForm
from django import forms
from adminapp.models import BookCategory,Book
from customer.models import Orders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryCreateForm(ModelForm):
    class Meta:
        model=BookCategory
        fields='__all__'
        widgets={
            'category_name':forms.TextInput(attrs={'class':'form-control'})
        }

class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
            'bookname': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

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
            "status":forms.HiddenInput(),
            "user": forms.HiddenInput(),


        }



class SearchForm(ModelForm):
    class Meta:
        model=Book
        fields=['bookname','author','category','language','publisher']



class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']





