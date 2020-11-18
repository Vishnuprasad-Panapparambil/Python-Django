from django.shortcuts import render,redirect
from adminapp.models import BookCategory,Book
from adminapp.forms import BookCreateForm,CategoryCreateForm,SearchAdminForm,OrderUpdateForm
from customer.models import Orders
from customer.forms import Orderform
from customer.filters import OrderFilter
from django.contrib.auth.decorators import login_required


def CreateCategory(request):

    form=CategoryCreateForm()
    context={}
    context['form']=form
    qs=BookCategory.objects.all()
    context['category']=qs

    if request.method=='POST':
        form=CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("createcategory")


    return render(request,"adminapp/create_category1.html",context)



def DeleteCategory(request,pk):
    ob=BookCategory.objects.get(id=pk).delete()
    return redirect("createcategory")



def EditCategory(request,pk):
    obj=BookCategory.objects.get(id=pk)
    form=CategoryCreateForm(instance=obj)
    context={}
    context['forms']=form
    if request.method == "POST":
        ob = BookCategory.objects.get(id=pk)
        form = CategoryCreateForm( instance=ob,data=request.POST)


        if form.is_valid():
            form.save()
            return redirect("createcategory")

    return render(request,"adminapp/categoryedit.html",context)




def CreateBook(request):

    form=BookCreateForm()
    context={}
    context['form']=form

    if request.method=="POST":
         form=BookCreateForm(request.POST,request.FILES)

         if form.is_valid():
             form.save()
             qs = Book.objects.last()
             context['books'] = qs

         return render(request, "adminapp/create_book.html", context)



    return render(request,"adminapp/create_book.html",context)



def AdminHomePage(request):

    books=Book.objects.all()
    categories=BookCategory.objects.all()
    count=BookCategory.objects.all().count()
    print(count)
    context={}
    context['books']=books
    context['categories']=categories


    return render(request,"adminapp/adminhome.html",context)


def BooksOnStock(request):

    context={}
    ob=Book.objects.all()
    context['allbooks']=ob
    form=OrderFilter()
    context['search']=form

    if request.method=='POST':

        obj = OrderFilter(request.POST, queryset=ob)
        print(obj)
        context['books'] = obj


        return render(request, "adminapp/onstockview.html",context)

    return render(request,"adminapp/onstockview.html",context)



def DeleteBook(request,pk):
    obj = Book.objects.get(id=pk).delete()

    return redirect("bookonstock")



def BookEdit(request,pk):
    obj = Book.objects.get(id=pk)
    forms=BookCreateForm(instance=obj)
    context={}
    context['form']=forms

    if request.method=="POST":
        ob = Book.objects.get(id=pk)
        form = BookCreateForm(instance=ob, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

        return redirect("bookonstock")



    return render(request, "adminapp/bookedit.html", context)




def BookView(request,pk):

    ob=Book.objects.get(id=pk)
    context={}
    context['books']=ob
    return render(request,"adminapp/bookview.html",context)




def AdminViewOrders(request):

    ob=Orders.objects.filter(active_status=1)

    context={}
    context['form']=ob

    return render(request,"adminapp/vieworders.html",context)





def OrderUpdates(request,pk):

    obj=Orders.objects.get(id=pk)
    form=OrderUpdateForm(instance=obj)
    context={}

    context['form']=form

    if request.method=="POST":
        form=Orderform(instance=obj,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminvieworders")

    return render(request,"adminapp/orderupdate.html",context)





def CancelledOrders(request):

    ob=Orders.objects.filter(active_status=0)
    context={}
    context['orders']=ob

    return render(request,"adminapp/cancelled.html",context)



