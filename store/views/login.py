from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from store.models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View



class LoginUser(View):
	return_url=None
	def get(self,request):
		cart=request.session.get('cart') # this is empty session object for not throwing the error while reomove cookies from browser
		if not cart: # if the session and cookies are empty then create an empty sesion object
			request.session['cart']={}
		LoginUser.return_url=request.GET.get('return_url') # with the class we are storing the returning url if the user is logout from the order page and want to login again this will take him to the order page where we have use the middleware
		
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
				if LoginUser.return_url:
					return HttpResponseRedirect(LoginUser.return_url) # here we use the HttpResponseRedirect because we can't pass the hold url to simple redirect
				else:
					LoginUser.return_url=None#we use None here to empty the url for the next time login
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


def cart_page(request):
	return render(request,'store/cart.html')