from django.urls import path
from users import views

urlpatterns=[
  path('',views.HomeView.as_view(),name='home_view'),
  path('register',views.UserRegisterView.as_view(),name='reg_view'),
  path('login',views.UserLoginView.as_view(),name='log_view'),
  path('logout',views.UserLogoutView.as_view(),name='logout_view'),
  path('detail/<int:id>',views.ProductDetailView.as_view(),name='detail_view'),
  path('cart/<int:id>',views.AddToCartView.as_view(),name='addcart_view'),
  path('cartlist',views.CartListView.as_view(),name='cartlist_view'),
  path('cartcancel',views.CartCancelView.as_view(),name='cartcancel_view'),
  path('placeorder/<int:id>',views.OrderPlaceView.as_view(),name='placeorder_view'),
  path('userorderlist',views.UserOrderListView.as_view(),name='userorderlist_view'),
  path('addreview/<int:id>',views.AddReview.as_view(),name='addreview_view'),
]