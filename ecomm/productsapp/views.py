from django.shortcuts import render
from productsapp.models import Product
from productsapp.models import Product1
from productsapp.models import kidsproduct

from productsapp.models import Review
from django.contrib.auth.models import User


# Create your views here.
def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'product/product-list.html', {'product_list':product_list})

def product_detail(request, id):
    product_details = Product.objects.get(pk = id)
    pro_ducts = Product.objects.all()
    return render(request, 'product/product-detail.html', {'product_details':product_details, 'pro_ducts':pro_ducts})


def eproduct_list(request):
    eproduct_list = Product1.objects.all()
    return render(request, 'product/electronic.html', {'eproduct_list':eproduct_list})

def electronic_detail(request, id):
    electronic_details = Product1.objects.get(pk = id)
    epro_ducts = Product1.objects.all()
    return render(request, 'product/eproduct-detail.html', {'electronic_details':electronic_details, 'epro_ducts':epro_ducts})


def babycloth(request):
    babycloth = kidsproduct.objects.all()
    return render(request, 'product/babycloth.html',{'babycloth':babycloth})

def babycloth_detail(request, id):
    babycloth_details = kidsproduct.objects.get(pk = id)
    babypro_ducts = kidsproduct.objects.all()
    return render(request, 'product/babycloth_detail.html', {'babycloth_details':babycloth_details, 'babypro_ducts':babypro_ducts})

def checkout(request):
    return render(request, 'product/checkout.html')



def reviews(request):
    if request.method=='GET':
        print(">>>",request.path)
        print('hello')
        # prod_id = request.GET.get('prod_id')
        # prod_id=2
        # product = Product.objects.get(pk = prod_id)
        # Comment = request.GET.get('Comment')
        # rate = request.GET.get('rate')
        # user = request.user
        # print(prod_id,Comment, rate)
    return redirect('/')



