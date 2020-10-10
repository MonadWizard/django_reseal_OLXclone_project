from django.shortcuts import render
from .models import Product
# Create your views here.

def productlist(request):
    products = Product.objects.all()

    context = {'products': products}
    template_name = 'product/product_list.html'
    return render(request,template_name, context)


def productdetail(request, id):
    print(id)
    product_id = Product.objects.get(id=id)

    context = {'product_id' : product_id}
    template_name = 'product/product_detail.html'
    return render(request,template_name, context)
















