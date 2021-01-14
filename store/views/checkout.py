from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer,Order
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer') # for saving the order we need the customer id which is saved in session so we can get that from session
        cart = request.session.get('cart') # here we are accessing the cart because we need all product in cart
        # here we are using list and cart keys because in the cart keys that is product key and list because we are accessing more then one element which is inform list
        products=self.get_product_by_id(list(cart.keys())) 

        for product in products: # we iterate the products because we need price and products to save that in order object
            # with quantity use the cart because we need a keys of every product to find the total quantity of products
            # also here we used Customer model because in order table we have the customer foreign key so we will call the model and through that call the customer because customer id is unique and all the process is done by the customer id
            order=Order(customer=Customer(id=customer),product=product,address=address,phone=phone,price=product.price,quantity=cart.get(str(product.id))) # use str because in product dic key is string value is number so we can't compare string and number       
            order.save()
        request.session['cart']={} # using empty dictonary because after check out we want to clear the cart data using session 
        return redirect('cart_page')

    def get_product_by_id(self,ids):
        return Products.objects.filter(id__in=ids) #here we id__in because we are not passing one id we are passing list of ids because one use can have more then one item in the carts

    