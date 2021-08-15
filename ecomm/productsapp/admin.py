from django.contrib import admin
from productsapp.models import Product
from productsapp.models import Product1
from productsapp.models import kidsproduct
# from productsapp.models import payment
# from productsapp.models import billing_address
from productsapp.models import Review
admin.site.register(Product)
admin.site.register(Product1)
admin.site.register(kidsproduct)
# admin.site.register(payment)
# admin.site.register(billing_address)
admin.site.register(Review)


# Register your models here.
