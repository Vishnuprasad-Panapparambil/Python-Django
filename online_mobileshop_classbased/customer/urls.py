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
from django.urls import path,include
from .views import Index,Details,Orderpage,Orderlist,Loginpage,Registration,SignOutCustomer,CancelOrder,CartList,Removecart


urlpatterns = [

    path('index/',Index.as_view(),name="index"),
    path('details/<int:pk>', Details.as_view(), name="details"),
    path('order/<int:pk>', Orderpage.as_view(), name="order"),
    path('orderlist', Orderlist.as_view(), name="orderlist"),

    path('',Loginpage.as_view(), name="loginpage"),
    path('registration',Registration.as_view(), name="registration"),
    path('customersignout',SignOutCustomer.as_view(), name="customersignout"),
    path('cancelorder/<int:pk>',CancelOrder.as_view(), name="cancelorder"),
    path('cartlist/',CartList.as_view(), name="cartlist"),
    path('removecart/<int:pk>',Removecart.as_view(), name="removecart"),

]
