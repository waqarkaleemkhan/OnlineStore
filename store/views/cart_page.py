from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products = self.get_product_by_id(ids)
        print(products)
        return render(request,'store/cart.html',{'products':products})



    def get_product_by_id(self,ids):
        return Products.objects.filter(id__in=ids) #here we id__in because we are not passing one id we are passing list of ids because one use can have more then one item in the carts
