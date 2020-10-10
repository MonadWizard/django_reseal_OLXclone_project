from django.urls import path
from . import views

urlpatterns = [
    path('', views.productlist, name='product_list'),
    path('<int:id>', views.productdetail, name='product_detail'),


]