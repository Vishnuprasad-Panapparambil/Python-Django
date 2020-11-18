from django.shortcuts import render,redirect,HttpResponseRedirect
from admin_side.models import Mobile,Brand
from .models import Orders,Cart
from django.views.generic import TemplateView
from .forms import Orderform,RegistrationForm,CartForm
from django.contrib.auth import authenticate,login,logout
from customer.filters import SearchForm


from admin_side.forms import MobileCreateFrm

# Create your views here.

class Index(TemplateView):
    model=Mobile
    template_name = "customer/index.html"
    form_class=SearchForm()
    context={}

    def get(self, request, *args, **kwargs):
        ob=self.model.objects.all()
        self.context['mobiles']=ob
        self.context['search']=self.form_class
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        print("inside post")
        ob = Mobile.objects.all()
        obj = SearchForm(request.POST,queryset=ob)
        self.context['mobilesearch']=obj
        self.context['search']=self.form_class
        return render(request,self.template_name,self.context)







class Details(TemplateView):

    model=Mobile

    template_name = "customer/details.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.model.objects.get(id=id)
        self.context['mobiles']=qs
        form=CartForm(initial={"productid":id,"user":request.user,"productname":qs.mobile_name})
        self.context['form']=form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        form = CartForm(request.POST)

        if Cart.objects.filter(user=request.user,productid=id).exists():

            return redirect("cartlist")

        else:
            if form.is_valid():
                form.save()
                return redirect("cartlist")



class Orderpage(TemplateView):

    model=Orders
    template_name = "customer/order_side.html"
    form_class=Orderform()
    context={}

    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        ob=Mobile.objects.get(id=id)
        print(id)
        form=Orderform(initial={"productid":id,"user":request.user,"product_name":ob.mobile_name})
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        ob=Mobile.objects.get(id=id)

        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"customer/order_success.html")
        else:
            form = Orderform(initial={"productid": id,"user":request.user,"product_name":ob.mobile_name})
            self.context['form'] = form
            return render(request, self.template_name, self.context)




class Orderlist(TemplateView):

    template_name = "customer/order_list.html"
    context={}
    def get(self, request, *args, **kwargs):
        mobiles=Orders.objects.filter(user=request.user,active_status=1)


        self.context['mobiles']=mobiles
        return render(request,self.template_name,self.context)




class Loginpage(TemplateView):

    form=RegistrationForm()
    template_name="customer/login_page.html"
    context={}

    def get(self, request, *args, **kwargs):

        self.context['form']=self.form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):

        username = request.POST.get("uname")
        password = request.POST.get("pwd")

        if ((username == "admin") & (password == "admin")):
            return redirect("admin_index")
        else:
            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("loginpage")


class Registration(TemplateView):
    form=RegistrationForm()
    template_name="customer/login_page.html"
    context={}

    def post(self, request, *args, **kwargs):
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("loginpage")

class SignOutCustomer(TemplateView):
    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect("loginpage")

class CancelOrder(TemplateView):

    model=Orders
    template_name = "customer/order_list.html"

    def get(self, request, *args, **kwargs):

        id=kwargs.get("pk")
        ob=self.model.objects.get(id=id)
        ob.active_status=0
        ob.save()
        return redirect("orderlist")






class CartList(TemplateView):


    template_name = "customer/cart_list.html"
    context = {}


    def get(self, request, *args, **kwargs):
        lst=[]
        mobiles=Cart.objects.filter(user=request.user,cart_status=1)

        self.context['mobiles']=mobiles



        return render(request,self.template_name,self.context)

class Removecart(TemplateView):

    template_name = "customer/cart_list.html"
    model=Cart

    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        ob=self.model.objects.get(id=id)
        ob.cart_status=0
        ob.save()
        return redirect("cartlist")

















