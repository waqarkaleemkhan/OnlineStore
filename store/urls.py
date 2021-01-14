from django.urls import path

from . import views
from .views import home,login,signup
from .views.login import logout_user
from .views.cart_page import Cart
from .views.checkout import Checkout
from .views.order import Orders
urlpatterns=[
	path('',home.Home.as_view(),name='home'),
	path('register',signup.registerUser.as_view(),name='register'),
	path('login',login.LoginUser.as_view(),name='login'),
	path('logout',logout_user,name='logout'),
	path('cart_page',Cart.as_view(),name='cart_page'),
	path('check_out',Checkout.as_view(),name="check_out"),
	path('orders_page',Orders.as_view(),name="order_page"),
]