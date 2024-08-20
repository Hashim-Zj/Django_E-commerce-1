from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,DeleteView,ListView
from users.forms import UserRegisterForm,UserLoginForm,AddToCartForm,OrderPlaceForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from owner.models import product,cart,orders
from django.core.mail import send_mail,settings
from .decorator import login_required
from django.utils.decorators import method_decorator

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

    cart_obj=cart.objects.filter(user=user,product_name=pro,status="in-cart")

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

@method_decorator(login_required)
class CartListView(ListView):
  model=cart
  template_name='cart_list.html'
  context_object_name="pro"

  def get_queryset(self):
    return cart.objects.filter(user=self.request.user).exclude(status="order-placed").order_by("-date")

class CartCancelView(View):
  def get(self,request):
    return redirect('home_view')
  
class OrderPlaceView(FormView):
  template_name='order_place.html'
  model=orders
  form_class=OrderPlaceForm

  def post(self,request,*args,**kwargs):
    in_cart=cart.objects.get(id=kwargs.get("id"))
    user=request.user
    email=user.email
    address=request.POST.get("address")
    phone=request.POST.get("phone")
    orders.objects.create(user=user,product_name=in_cart,address=address,phone=phone)
    in_cart.status="order-placed"
    in_cart.save()
    send_mail("E-Bay.com","Your order placed Successful!",settings.EMAIL_HOST_USER,[email])
    messages.success(request,"order placed successful")
    return redirect('cartlist_view')
  
class UserOrderListView(View):

  def get(self,request):
    all_orders=orders.objects.filter(user=request.user).order_by("-date")
    deliverd=orders.objects.filter(user=request.user,status="delivered")
    return render(request,'user_order_list.html',{"all_orders":all_orders,"deliverd":deliverd})