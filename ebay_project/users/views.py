from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,DeleteView,ListView
from users.forms import UserRegisterForm,UserLoginForm,AddToCartForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from owner.models import product,cart


# Create your views here.

class HomeView(TemplateView):
  template_name='index.html'

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context["pro"]=product.objects.all()
    return context


class UserRegisterView(CreateView):
  template_name='user_register.html'
  form_class=UserRegisterForm
  success_url=reverse_lazy('home_view')


class UserLoginView(FormView):
  template_name='user_login.html'
  form_class=UserLoginForm

  def post(self, request):
    uname=request.POST.get("username")
    psw=request.POST.get("password")
    user=authenticate(request,username=uname,password=psw)
    if user:
      login(request,user)
      messages.success(request,"Login Successful")
      return redirect("home_view")
    else:
      messages.success(request,"Invalid credaintials")
      return redirect("home_view")

class UserLogoutView(View):
  def get(self,request):
    logout(request)
    messages.success(request,"Logout Successful")
    return redirect("home_view")

class ProductDetailView(DeleteView):
  template_name="produc_detail.html"
  model=product
  pk_url_kwarg="id"
  context_object_name="pro"

class AddToCartView(View):
  def get(self, request,*args,**kwargs):
    pro=product.objects.get(id=kwargs.get("id"))
    form=AddToCartForm()
    return render(request, "add_to_cart.html",{"pro":pro,"form":form})

  def post(self,request,*args,**kwargs):
    user=request.user
    pro=product.objects.get(id=kwargs.get("id"))
    qty=request.POST.get("quantity")

    cart_obj=cart.objects.filter(user=user,product_name=pro)

    if cart_obj:
      cart_pro=cart_obj[0]
      cart_pro.quantity+=int(qty)
      cart_pro.save()

      messages.success(request,"Product Added to cart")
      return redirect("home_view")
    
    else:
      cart.objects.create(user=user,product_name=pro,quantity=qty)
      messages.success(request,"Product Added to cart")
      return redirect("home_view")


class CartListView(ListView):
  model=cart
  template_name='cart_list.html'
  context_object_name="pro"

  def get_queryset(self):
    return cart.objects.filter(user=self.request.user)