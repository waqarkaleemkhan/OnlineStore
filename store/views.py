from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
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

def validateUser(customer,email):
	error_message=None
	if(not customer.first_name):
		error_message='First Name Required'
	elif len(customer.first_name) < 3:
		error_message='First Name must be 3 charcter or more'
	elif(not customer.last_name):
		error_message='Last Name Required'
	elif len(customer.last_name) < 3:
		error_message='Last Name must be 3 charcter or more'
	elif(not customer.password):
		error_message='Password Required'
	elif len(customer.password) < 6:
		error_message='Password must be 6 charcter or more'
	elif(not customer.phone):
		error_message='Phone number Required'
	elif len(customer.phone) < 11:
		error_message='Phone number must be 11 charcter or more'
	elif isEmailExist(email):
		error_message='Email Already Register'
	return error_message



def registerUser(request):
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		address=request.POST.get('address')
		password=request.POST.get('password')

		value = {'first_name':first_name,'last_name':last_name,'email':email,'phone':phone,'address':address}

		error_message=None
		customer=Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,password=password)
		error_message=validateUser(customer,email)
		
		if(not error_message):
			customer.password=make_password(customer.password)
			customer.save()
			return redirect('home')
		else:
			context={'error':error_message,'values':value}
			return render(request,'store/register.html',context)
def get_all_product_by_categoryid(category_id):
	if category_id:
		return Products.objects.filter(category=category_id)
	else:
		return Products.objects.all()


def register(request):
	if request.method=='GET':
		return render(request,'store/register.html')
	else:
		return registerUser(request)
	

def isEmailExist(email):
	if Customer.objects.filter(email=email):
		return True
	return False



def loginUser(request):
	if request.method=='GET':
		return render(request,'store/login.html')
	elif request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		customer=getCustomerByEmail(email) #taking customer object email and through that email we check the hash password
		error_message=None
		if customer:
			flag=check_password(password,customer.password)
			if flag:
				return redirect('home')
			else:
				error_message='Email or Password is Invalid'
		else:
			error_message='Email or Password is Iinvalid'
		return render(request,'store/login.html',{'error':error_message})


def getCustomerByEmail(email): #getting user email
	try:
		return Customer.objects.get(email=email)
	except:
		return False