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


