from django.urls import path
from . import views

urlpatterns = [
  path('dashbord',views.AdminView.as_view(),name='dashbord_view'),
  path('orderlist',views.OrderListView.as_view(),name='orderlist_view'),
  path('orderdetail/<int:id>',views.OrderDetailView.as_view(),name='orderdetail_view'),
   
]

