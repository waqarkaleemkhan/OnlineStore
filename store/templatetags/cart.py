from django import template
register = template.Library() # register is a decorater and it will be in templates library

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys() #key is the values of of products in cart which is like a dictonary 
    for id in keys:
        if int(id)==product.id: # id in the dictionary is inform of string so we converti it into the int
            return True
    return False

@register.filter(name='cart_count')
def cart_count(product,cart):
    keys=cart.keys() #key is the values of of products in cart which is like a dictonary 
    for id in keys:
        if int(id)==product.id: # id in the dictionary is inform of string so we converti it into the int
            return cart.get(id) #this will return the quantity base on the id which is the number of times the product is added to cart
    return False

# this filter is for calculating total price of one type of product
@register.filter(name='product_total_price')
def product_total_price(product,cart):
   return product.price*cart_count(product,cart) #here we are counting the total price of products because we can't do mathematicaloperations
   # in the templates and we call the cart_count filter and to it we pass cart and product

# this filter is for calculating total price of cart
@register.filter(name="cart_total_price")
def cart_total_price(products, cart): # we pass cart because we are using the above product_total_price cart and the products is for the list because we are calculating the total cart price so we are will pass the list in it
    sum=0
    for p in products:
        sum+=product_total_price(p,cart) # p will give us single product from loop iterations and the cart is because of using cart function
    return sum