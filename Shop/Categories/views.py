from django.shortcuts import render
from .models import Category
from Products.models import Product
# Create your views here.
def show_categories(request):
    category = Category.objects.all()
    context = {'categories': category}
    return render(request=request, template_name= 'categories.html', context= context)

def show_products_from_category(request,category_name):
    # category_filtered = Category.objects.filter(name = category_name)
    # print(category_filtered[0])
    product = Product.objects.filter(category__name = category_name)
    context = {'products': product}
    return render(request=request, template_name='products.html', context= context)