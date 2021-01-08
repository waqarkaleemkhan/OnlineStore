from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.

def Home(request):
	products=Products.objects.all()
	context={'products':products}
	return render(request,'store/home.html',context)