from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class registerUser(View):
	def get(self,request):
		return render(request,'store/register.html')
	def post(self,request):
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		address=request.POST.get('address')
		password=request.POST.get('password')

		value = {'first_name':first_name,'last_name':last_name,'email':email,'phone':phone,'address':address}

		error_message=None
		customer=Customer(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,password=password)
		error_message=self.validateUser(customer,email)
		
		if(not error_message):
			customer.password=make_password(customer.password)
			customer.save()
			return redirect('home')
		else:
			context={'error':error_message,'values':value}
			return render(request,'store/register.html',context)
	def validateUser(self,customer,email): # validating signup form fields
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
		elif len(customer.phone) < 11 or len(customer.phone)>14:
			error_message='Phone number must be 11 charcter or more'
		elif self.isEmailExist(email):
			error_message='Email Already Register'
		return error_message
	def isEmailExist(self,email): # checking customer email in database if exist then throw error that email already exists
		if Customer.objects.filter(email=email):
			return True
		return False