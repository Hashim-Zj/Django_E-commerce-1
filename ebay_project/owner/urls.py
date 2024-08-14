from django.urls import path
from .views import AdminView

urlpatterns = [
  path('dashbord',AdminView.as_view(),name='dashbord_view'),
   
]

