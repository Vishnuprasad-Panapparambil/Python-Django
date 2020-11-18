from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from admin_side.forms import BrandCreateForm,MobileCreateFrm,OrderupdateFrm
from .models import Brand,Mobile
from customer.models import Orders,Cart
from django.contrib.auth import logout
from django.db.models import Count



# Create your views here.

class Admin_Index(TemplateView):
    model=Mobile
    template_name = "admin_side/admin_index.html"

    context={}

    def get(self, request, *args, **kwargs):
        ob=self.model.objects.all()
        self.context['mobiles']=ob
        return render(request,self.template_name,self.context)

class Details_view(TemplateView):

    model=Mobile

    template_name = "admin_side/details_view.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.model.objects.get(id=id)
        self.context['mobiles']=qs
        return render(request, self.template_name, self.context)




class CreateBrand(TemplateView):

    form=BrandCreateForm()
    context={}
    model=Brand
    template_name="admin_side/create_brand.html"

    def get(self,request,*args,**kwargs):
        qs=self.model.objects.all()
        self.context['brands']=qs
        self.context['form']=self.form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=BrandCreateForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect("brandcreate")

        return redirect("brandcreate")

class  EditBrand(TemplateView):


    context={}
    model=Brand
    template_name="admin_side/create_brand.html"

    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj=self.model.objects.get(id=id)
        qs=self.model.objects.all()
        self.context['brands']=qs
        form=BrandCreateForm(instance=obj)
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):

        id = kwargs.get("pk")
        ob = self.model.objects.get(id=id)
        form=BrandCreateForm(instance=ob,data=request.POST)
        if form.is_valid():
                form.save()
                return redirect("brandcreate")

        return redirect("brandcreate")


class DeleteBrand(TemplateView):



    model=Brand
    template_name="admin_side/create_brand.html"

    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj=self.model.objects.get(id=id).delete()
        return redirect("brandcreate")


class CreateMobile(TemplateView):
    model=Mobile
    form=MobileCreateFrm()
    template_name = "admin_side/create_mobile.html"
    context={}

    def get(self, request, *args, **kwargs):
        self.context['form']=self.form
        mobiles= self.model.objects.all()
        self.context['mobiles']=mobiles
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=MobileCreateFrm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("mobilecreate")


class Editmobile(TemplateView):
    model=Mobile
    form=MobileCreateFrm()
    template_name = "admin_side/create_mobile.html"
    context={}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        obj=self.model.objects.get(id=id)
        form=MobileCreateFrm(instance=obj)
        self.context['form']=form
        mobiles= self.model.objects.all()
        self.context['mobiles']=mobiles
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        ob = self.model.objects.get(id=id)
        form=MobileCreateFrm(instance=ob, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("mobilecreate")


class Deletemobile(TemplateView):
    model=Mobile
    template_name = "admin_side/create_mobile.html"
    context={}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        obj=self.model.objects.get(id=id).delete()
        return redirect("mobilecreate")


class Viewmobile(TemplateView):
    model=Mobile
    template_name = "admin_side/mobileview.html"
    context={}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        obj=self.model.objects.get(id=id)
        self.context['mobiles']=obj
        return render(request,self.template_name,self.context)

class Vieworeders(TemplateView):

    template_name = "admin_side/orderslist.html"
    context={}
    form=OrderupdateFrm()
    model=Orders
    def get(self, request, *args, **kwargs):
        mobiles=self.model.objects.filter(active_status=1)
        self.context['mobiles']=mobiles
        self.context['form']=self.form
        return render(request,self.template_name,self.context)

class Orderupdate(TemplateView):
    template_name = "admin_side/orderslist.html"
    context={}
    model=Orders

    def get(self, request, *args, **kwargs):

        id=kwargs.get("pk")
        mobiles=self.model.objects.filter(active_status=1)
        self.context['mobiles']=mobiles
        obj=self.model.objects.get(id=id)
        self.context['form']=OrderupdateFrm(instance=obj)
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        ob = self.model.objects.get(id=id)
        form=OrderupdateFrm(instance=ob, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("vieworders")



class SignOut(TemplateView):
    def get(self, request, *args, **kwargs):

        logout(request)

        return redirect("loginpage")

class Sales(TemplateView):

    template_name = "admin_side/sales.html"
    context={}

    def get(self, request, *args, **kwargs):

        ob = Cart.objects.values('productname').annotate(Count('productname'))
        self.context['carted']=ob
        obj = Orders.objects.exclude(status="deliverd").values('product_name').annotate(Count('product_name'))
        self.context['pending']=obj
        qs= Orders.objects.filter(status="deliverd").values('product_name').annotate(Count('product_name'))
        self.context['delivered']=qs
        return render(request,self.template_name,self.context)

















