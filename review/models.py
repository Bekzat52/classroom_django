from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='review', on_delete=models.CASCADE)
    text = models.TextField()
    
    def get_avarage_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

