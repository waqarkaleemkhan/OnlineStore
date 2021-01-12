from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View



def Home(request):
	products=None
	categories=Category.objects.all()
	categoryID=request.GET.get('category') #getting products by category
	if categoryID:
		products=get_all_product_by_categoryid(categoryID)
	else:
		products=Products.objects.all()
	context={'products':products,'categories':categories}
	return render(request,'store/home.html',context)


def get_all_product_by_categoryid(category_id):
	if category_id:
		return Products.objects.filter(category=category_id)
	else:
		return Products.objects.all()
