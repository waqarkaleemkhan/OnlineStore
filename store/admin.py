from django.contrib import admin
from .models import Products,Category
# Register your models here.

class AdminProduct(admin.ModelAdmin):
	list_display=['name','price','category']
class AdminCategory(admin.ModelAdmin):
	list_display=['name']
admin.site.register(Products,AdminProduct)
admin.site.register(Category,AdminCategory)
