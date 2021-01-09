from django.db import models

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name
class Products(models.Model):
	name=models.CharField(max_length=50)
	price=models.IntegerField(default=0)
	category=models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
	description=models.CharField(max_length=200,null=True, blank=True)
	image=models.ImageField(upload_to = 'uploads/products/')

class Customer(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField()
	phone=models.CharField(max_length=15)
	address=models.CharField(max_length=200)
	password=models.CharField(max_length=500)


