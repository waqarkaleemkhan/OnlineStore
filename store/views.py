from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products,Category,Customer
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
	if request.method=='GET':
		return render(request,'store/register.html')
	else:
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		address=request.POST.get('address')
		password=request.POST.get('password')

		value = {'first_name':first_name,'last_name':last_name,'email':email,'phone':phone,'address':address}

		error_message=None
		if(not first_name):
			error_message='First Name Required'
		elif len(first_name) < 3:
			error_message='First Name must be 3 charcter or more'
		elif(not last_name):
			error_message='Last Name Required'
		elif len(last_name) < 3:
			error_message='Last Name must be 3 charcter or more'
		elif(not password):
			error_message='Password Required'
		elif len(password) < 6:
			error_message='Password must be 6 charcter or more'
		elif(not phone):
			error_message='Phone number Required'
		elif len(phone) < 11:
			error_message='Phone number must be 11 charcter or more'
		if(not error_message):
			customer=Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,password=password)
			customer.save()
			return redirect('home')
		else:
			context={'error':error_message,'values':value}
			return render(request,'store/register.html',context)
