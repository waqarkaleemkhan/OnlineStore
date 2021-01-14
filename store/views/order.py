from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Products,Category,Customer,Order
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Orders(View):
    def get(self,request):
        customer=request.session.get('customer')
        orders=self.get_order_by_customer(customer)
        return render(request,'store/orders.html',{'orders':orders})
    def get_order_by_customer(self,customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')