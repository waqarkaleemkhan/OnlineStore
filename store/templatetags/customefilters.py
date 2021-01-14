from django import template
register = template.Library() # register is a decorater and it will be in templates library
@register.filter(name='currency')
def currency(number):
    return "PKR "+str(number)

