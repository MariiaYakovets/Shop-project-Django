"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Products.views import show_products, show_product, create_product, upload_products
from Categories.views import show_categories, show_products_from_category
from django.conf import settings
from django.conf.urls.static import static
from Users.views import show_user, login_user,change_password, register_user, loguot_user, show_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main_page, name= 'main'),
    path('categories/', show_categories, name= 'categories'),
    path('products/', show_products, name= 'products'),
    path('category/<str:category_name>', show_products_from_category, name = 'category'),
    path('product/<int:product_pk>', show_product, name = 'product' ),
    path('user/', show_user, name= 'user'),
    path('user/login/', login_user, name='login'),
    path('user/register/', register_user, name='registration'),
    path('user/logout', loguot_user, name='logout'),
    path('user/change-password', change_password, name='change-password'),
    path('products/create-product/', create_product, name= 'create-product'),
    path('product/upload-products', upload_products, name= 'upload-products')
]+ static(settings.STATIC_URL)

