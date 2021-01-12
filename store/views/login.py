from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View



class LoginUser(View):
	def get(self,request):
		return render(request,'store/login.html')
	def post(self,request):
		email=request.POST.get('email')
		password=request.POST.get('password')
		customer=self.getCustomerByEmail(email) #taking customer object email and through that email we check the hash password
		error_message=None
		if customer: #if customer with email object exist the check customer password
			flag=check_password(password,customer.password) #checking customer password with hash password and if return true customer redirect to home page
			if flag:
				request.session['customer']=customer.id
				# request.session['email']=customer.email we don't need email here because we can do things on customer id which is unique
				return redirect('home')
			else:
				error_message='Email or Password is Invalid'
		else:
			error_message='Email or Password is Iinvalid'
		return render(request,'store/login.html',{'error':error_message})

	def getCustomerByEmail(self,email): #getting user email
		try:
			return Customer.objects.get(email=email)
		except:
			return False


def logout_user(request):
	request.session.clear()
	return redirect('login')