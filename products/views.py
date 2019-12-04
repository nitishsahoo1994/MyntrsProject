from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
    context={'user':'Nitish'}
    template='products/base.html'
    return render(request,template,context)

def product(request):
    context={'product_name':Product.objects.all()}
    template='products/product.html'
    return render(request, template ,context)