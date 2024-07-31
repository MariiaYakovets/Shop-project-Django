from django.shortcuts import render
from.models import Product
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