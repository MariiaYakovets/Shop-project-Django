from django.shortcuts import render, redirect
from.models import Product
from django.http import HttpResponse
import json
from Categories.models import Category
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pandas
from spire.xls import *
from spire.xls.common import *

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

def upload_products(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        path = default_storage.save('tmp/file.xlsx', ContentFile(uploaded_file.read()))
        file = pandas.read_excel(io= path, sheet_name= 'Sheet1')
        columns = file.columns.ravel() #list
        columns = columns[1:6] #list
        columns = columns.tolist() 
        list= []
        for column in columns:
            list_data = []
            for cell in file[column]:
                list_data.append(cell)
            list.append(list_data)
        list_products = []
        for index in range(len(list[0])):
            list_data = []
            for product_set in list:
                list_data.append(product_set[index])
            list_products.append(list_data)
        # print(list_products)
        del list_products[0]

        categories = Category.objects.all()
        category_names = []
        for category in categories:
            # взяли и сделали список чисто имен категорий
            category_names.append(category.name)

        for product_data in list_products:
            print(product_data)
            # only if it is a new category
            # тк product_data[3]- строка, сравниваем теперь со списком строк category_names
            if product_data[3] not in category_names:
                new_category = Category.objects.create(
                    name = product_data[3])
                new_category.save()
                # обновление списка существующих имен категорий
                category_names.append(new_category.name)

            #create a product from file data obtained above    
            product = Product.objects.create(
                name = product_data[0],
                price = int(product_data[1]),
                description = product_data[2],
                image = product_data[4],
                category = Category.objects.filter(name = product_data[3]).first())
            product.save()
        return redirect('categories')


          
    elif request.method == 'GET':
        return render(request=request, template_name= 'upload_products.html')