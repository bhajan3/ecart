from django.db import models
from django.contrib.auth.models import User
import datetime

# test git commits..

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    specification = models.TextField( null = True)

    def __str__(self):
        return str(self.image)

class Product1(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    specification = models.TextField(null=True)

    def __str__(self):
        return str(self.image)


class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    Comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.id)

class kidsproduct(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images')
    specification = models.TextField( null = True)

    def __str__(self):
        return str(self.image)

# class billing_address(models.Model):
#     user = models.ForeignKey(User, models.CASCADE)
#     first_name = models.CharField(max_length=254)
#     last_name = models.CharField(max_length=254)
#     date = models.DateTimeField( auto_now_add= True )
#     email = models.CharField(max_length=50)
#     mobile_no = models.CharField(max_length=20)
#     address = models.CharField(max_length=254)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     zip_code = models.CharField(max_length=50)
#
#     def __str__(self):
#         return str(self.first_name)
#
# class payment(models.Model):
#     CHOICES = (
#         ('py', 'Paypal'),
#         ('cp', 'Check Payment'),
#         ('dbt', 'Direct Bank Transfer'),
#         ('ct', 'Cash on Delivery'),
#     )
#     user = models.ForeignKey(User, models.CASCADE)
#     payment_type = models.CharField(max_length=300,choices= CHOICES)
#
#     def __str__(self):
#         return str(self.payment_type)
















