from django.shortcuts import render
from .models import Product, ProductImages

from django.core.paginator import Paginator

# Create your views here.

def productlist(request):
    products = Product.objects.all()  # product_list

    # pagination
    paginator = Paginator(products, 1) # Show 25 contacts per page.
    page = request.GET.get('page') #page
    products = paginator.get_page(page)

    context = {'products': products}
    template_name = 'product/product_list.html'
    return render(request,template_name, context)


def productdetail(request, product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)

    context = {'product_detail' : productdetail, 'product_images' : productimages}
    template_name = 'product/product_detail.html'
    return render(request,template_name, context)
















