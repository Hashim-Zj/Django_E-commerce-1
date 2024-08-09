from django.urls import path
from users import views

urlpatterns=[
  path('',views.HomeView.as_view(),name='home_view'),
  path('register',views.UserRegisterView.as_view(),name='reg_view'),
  path('login',views.UserLoginView.as_view(),name='log_view'),
  path('logout',views.UserLogoutView.as_view(),name='logout_view'),
  path('detail/<int:id>',views.ProductDetailView.as_view(),name='detail_view'),
]