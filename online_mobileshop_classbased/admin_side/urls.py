"""online_mobileshop_classbased URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import CreateBrand,CreateMobile,Editmobile,Deletemobile,Viewmobile,Vieworeders,Orderupdate,Admin_Index,Details_view,EditBrand,DeleteBrand,SignOut,Sales

urlpatterns = [

    path('brandcreate/',CreateBrand.as_view(),name='brandcreate'),
    path('mobilecreate/',CreateMobile.as_view(),name='mobilecreate'),
    path('editmobile/<int:pk>',Editmobile.as_view(),name='editmobile'),
    path('deletemobile/<int:pk>',Deletemobile.as_view(), name='deletemobile'),
    path('viewmobile/<int:pk>',Viewmobile.as_view(), name='viewmobile'),
    path('vieworders/',Vieworeders.as_view(), name='vieworders'),
    path('orderupdate/<int:pk>',Orderupdate.as_view(), name='orderupdate'),
    path('admin_index',Admin_Index.as_view(), name='admin_index'),
    path('view/<int:pk>',Details_view.as_view(), name='view'),
    path('editbrand/<int:pk>',EditBrand.as_view(), name='editbrand'),
    path('deletebrand/<int:pk>',DeleteBrand.as_view(), name='deletebrand'),
    path('signout/',SignOut.as_view(), name='signout'),
    path('sales/',Sales.as_view(), name='sales'),

]
