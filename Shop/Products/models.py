from django.db import models
from Categories.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    def __str__(self):
        return self.name
    