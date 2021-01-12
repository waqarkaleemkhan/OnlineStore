from django.urls import path

from . import views
from .views import home,login,signup
urlpatterns=[
	path('',home.Home,name='home'),
	path('register',signup.registerUser.as_view(),name='register'),
	path('login',login.LoginUser.as_view(),name='login'),
]