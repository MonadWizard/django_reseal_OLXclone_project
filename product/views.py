from django.shortcuts import render
from .models import Product, ProductImages, Category

from django.core.paginator import Paginator
from django.db.models import Count # for count all data each category

# for search we use   Complex lookups with Q objects
from django.db.models import Q


from django.shortcuts import get_object_or_404 

# Create your views here.

def productlist(request, category_slug=None):
    category = None
    products = Product.objects.all()  # product_list
    categories = Category.objects.annotate(total_products=Count('product'))  #count data on each category_list

    # display items by clicking on category
    if category_slug:
        category = get_object_or_404(Category, slug= category_slug)
        products = products.filter(category=category)
    
    # filter for search
    search_query = request.GET.get('q')
    if search_query :
        products = products.filter(
            Q(name__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(created__icontains = search_query)

        )



    # pagination
    paginator = Paginator(products, 3) # Show 25 contacts per page.
    page = request.GET.get('page') 
    products = paginator.get_page(page)


    context = {'products': products, 'categories':categories, 'category': category }
    template_name = 'product/product_list.html'
    return render(request,template_name, context)


def productdetail(request, product_slug):
    productdetail = Product.objects.get(slug=product_slug)  # pick specific products
    productimages = ProductImages.objects.filter(product=productdetail)



    context = {'product_detail' : productdetail, 'product_images' : productimages}
    template_name = 'product/product_detail.html'
    return render(request,template_name, context)
















