from django.shortcuts import render
from productsapp.models import Product
from productsapp.models import Product1

# Create your views here.

def index(request):
	Recent_pro = Product.objects.all()
	elec_prod =  Product1.objects.all()
	return render(request, 'home/index.html', {'Recent_pro':Recent_pro, 'elec_prod':elec_prod})
