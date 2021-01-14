from django.urls import path
from store.middlewares.authmiddleware import auth_middleware

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
	path('orders_page',auth_middleware(Orders.as_view()),name="order_page"), #here we can use the middleware also
]