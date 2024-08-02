from django.shortcuts import render, redirect
from.models import Product
from django.http import HttpResponse
import json
from Categories.models import Category
# Create your views here.
def show_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request= request, template_name= 'products.html', context=context)

def show_product(request, product_pk):
    products = Product.objects.all()
    product = products.filter(id = product_pk)
    print(product)
    context = {'product': product.first()}
    return render( request= request, template_name= 'product_page.html', context= context)

def create_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            byte_data = request.body
            data = json.loads(byte_data.decode("utf-8"))
            print(data)
            name = data['name']
            price = data['price']
            description = data['description']
            image = data['image']
            category = Category.objects.filter(name= data['category']).first()
            new_product = Product.objects.create(name= name, price= price, description= description, image= image, category=category)
            new_product.save()
            return HttpResponse(status=200, reason="Product has been successfully created")
        
        elif request.method == 'GET':
            categories = Category.objects.all()
            context = {'categories': categories}
            return render(request=request, template_name='create_product.html', context= context)
    else:
        return redirect('login')
