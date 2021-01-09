from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Category
# Create your views here.

def Home(request):
	products=None
	categories=Category.objects.all()
	categoryID=request.GET.get('category')
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


def register(request):
	return render(request,'store/register.html')