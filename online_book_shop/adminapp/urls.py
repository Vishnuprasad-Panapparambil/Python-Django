"""online_book_shop URL Configuration

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

from django.urls import path
from adminapp.views import CreateCategory,CreateBook,AdminHomePage,BooksOnStock,DeleteBook,BookEdit,BookView,DeleteCategory,EditCategory,AdminViewOrders,OrderUpdates,CancelledOrders

urlpatterns = [
    path('createcategory',CreateCategory,name="createcategory"),
    path('deletecategory/<int:pk>',DeleteCategory,name="deletecategory"),
    path('editcategory/<int:pk>',EditCategory,name="editcategory"),
    path('createbook',CreateBook,name="createbook"),
    path('',AdminHomePage,name="adminhome"),
    path('bookonstock',BooksOnStock,name="bookonstock"),
    path('deletebook/<int:pk>',DeleteBook,name="deletebook"),
    path('bookedit/<int:pk>',BookEdit,name="bookedit"),
    path('bookview/<int:pk>',BookView,name="bookview"),
    path('adminvieworders',AdminViewOrders,name="adminvieworders"),
    path('orderupdates/<int:pk>',OrderUpdates,name="orderupdates"),
    path('cancelledorders',CancelledOrders,name="cancelledorders"),

]
