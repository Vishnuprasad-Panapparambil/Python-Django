
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from adminapp.models import BookCategory,Book
from customer.models import Orders
from adminapp.forms import BookCreateForm,CategoryCreateForm
from customer.forms import Orderform,SearchForm,RegistrationForm
from customer.filters import OrderFilter
from django.contrib.auth.decorators import login_required

username=''

@login_required(login_url='loginpage')
def CostomerHomePage(request):

    books=Book.objects.all()
    categories=BookCategory.objects.all()
    count=BookCategory.objects.all().count()
    print(count)
    context={}
    context['books']=books
    context['categories']=categories
    form=SearchForm()
    context['search']=form





    return render(request,"customer/customer_home.html",context)

@login_required(login_url='loginpage')
def DetailsViewPage(request,pk):

    ob=Book.objects.get(id=pk)
    context={}
    context['books']=ob
    return render(request,"customer/bookdetails.html",context)

@login_required(login_url='loginpage')
def Order (request,pk):
    context={}
    form=Orderform(initial={"productid":pk,"user":request.user})
    context['form']=form
    if request.method=="POST":
        form=Orderform(request.POST)
        if form.is_valid():
            form.save()
            print("iam here")
            return render(request,"customer/ordersuccess.html")

    return render(request,"customer/purchasedetails.html",context)

@login_required(login_url='loginpage')
def ViewOrder(request):

    context={}
    ob=Orders.objects.filter(user=request.user,active_status=1)
    for i in ob:
        print(i.productid)

    obj=Book.objects.all()
    context['form']=ob
    context['books']=obj


    return render(request,"customer/vieworders.html",context)



@login_required(login_url='loginpage')
def Cancelorder(request,pk):

    ob=Orders.objects.get(id=pk)
    ob.active_status=0
    ob.save()

    return redirect("vieworder")



@login_required(login_url='loginpage')
def SearchBook(request):


    ob=Book.objects.all()
    form=OrderFilter()
    context={}
    context['search']=form
    context['bookcollection'] = ob




    if request.method=='POST':
        obj = OrderFilter(request.POST,queryset=ob)

        context['books']=obj
        return render(request, "customer/search.html", context)



    return render(request, "customer/search.html", context)




def register(request):

    form=RegistrationForm()
    context={}
    context['form']=form

    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"customer/login.html")


    return render(request, "customer/registration.html", context)



def loginpage(request):

    if request.method=='POST':
        username=request.POST.get("uname")
        password=request.POST.get("pwd")


        if((username=="admin")&(password=="admin")):
            return redirect("adminhome")
        else:
            user=authenticate(request,username=username,password=password)
            print(user)

            if user is not None:
                login(request,user)
                return redirect("homepage")
            else:
                return redirect("loginpage")

    return render(request,"customer/login.html")



@login_required(login_url='loginpage')
def signout(request):

    logout(request)

    return redirect("loginpage")







