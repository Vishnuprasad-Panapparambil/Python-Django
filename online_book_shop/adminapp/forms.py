from django.forms import ModelForm
from django import forms
from adminapp.models import BookCategory,Book
from customer.models import Orders

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
            'cart_status': forms.HiddenInput(),

        }

class SearchAdminForm(ModelForm):
    class Meta:
        model=Book
        fields=['category']


class OrderUpdateForm(ModelForm):

    class Meta:
        model=Orders
        fields = '__all__'
        widgets={
            'bookname': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }