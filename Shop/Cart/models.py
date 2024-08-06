from django.db import models
from Products.models import Product
from django.contrib.auth.models import User
# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    data_added = models.DateTimeField(auto_now_add=True)

    