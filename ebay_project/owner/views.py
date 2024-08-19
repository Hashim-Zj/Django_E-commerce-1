from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import orders
from .forms import OrderDetailsForm
from django.core.mail import send_mail,settings
from django.contrib import messages
from django.contrib.auth.models import User

class AdminView(TemplateView):
  template_name="admin.html"

  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    context["orders"]=orders.objects.filter(status="order-placed").count()
    return context

class OrderListView(ListView):
  template_name="order_list.html"
  model=orders
  context_object_name="orders"

  def get_queryset(self):
    return orders.objects.filter(status="order-placed")
  
class OrderDetailView(DetailView):
  template_name="order_detail.html"
  model=orders
  context_object_name="order"
  pk_url_kwarg="id"

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['form']=OrderDetailsForm()
    return context
  
  def post(self,request,*args,**kwargs):
    status=request.POST.get("status")
    date=request.POST.get("expected_date")
    order=orders.objects.get(id=kwargs.get("id"))
    order.status=status
    order.expected_delivery_date=date
    order.save()
    user=User.objects.get(id=order.user_id)
    res=send_mail("Conformation Mail",f"Expected delivery at {date}",settings.EMAIL_HOST_USER,[user.email])
    if res==1:
      return redirect ('orderlist_view')
    else:
      messages.warning(request,"somethings wrong")
      return redirect("orderlist_view")