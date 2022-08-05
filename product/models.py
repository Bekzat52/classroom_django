from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='product')
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
