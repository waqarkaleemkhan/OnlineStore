from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Home(View):
	def post(self,request): # getting post request for saving product to cart
		product = request.POST.get('product')
		remove=request.POST.get('remove') # subtract one from the cart value while clicking on the - button
		cart = request.session.get('cart') # storing cart data into session
		if cart: # if the cart is already avalible in the session so we will append the cart and if the card is not then we add it throgh the else condition
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity<=1:
						cart.pop(product)
					else:
						cart[product]=quantity-1
				else:
					cart[product]=quantity+1 # the product is the id value to which one value will be added
			else:
				cart[product]=1
		else:
			cart={} # if the cart is not existing then create a an empty dic and add to it the cart
			cart[product]=1
		request.session['cart']=cart #now saving the value of cart to a cart in last using object
		print(request.session['cart'])
		return redirect('home')


	
		
	def get(self,request):
		cart=request.session.get('cart') # this is empty session object for not throwing the error while reomove cookies from browser
		if not cart: # if the session and cookies are empty then create an empty sesion object
			request.session['cart']={}
		products=None
		categories=Category.objects.all()
		categoryID=request.GET.get('category') #getting products by category
		if categoryID:
			products=self.get_all_product_by_categoryid(categoryID)
		else:
			products=Products.objects.all()
		context={'products':products,'categories':categories}
		return render(request,'store/home.html',context)

	def get_all_product_by_categoryid(self,category_id):
		if category_id:
			return Products.objects.filter(category=category_id)
		else:
			return Products.objects.all()
