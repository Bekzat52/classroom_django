from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product, Rating, Review
from rest_framework.viewsets import GenericViewSet

from rest_framework.response import Response
from rest_framework import mixins

class ReviewViewSet(mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    queryset = Review.objects.all()


@api_view
def add_rating(request, p_id):
    user = request.user
    value = request.POST.get('value')
    product = get_object_or_404(Product, id=p_id)

    if Rating.objects.filter(user=user, product=product).exists():
        rating = Rating.objects.get(user=user, product=product)
        rating.value = value
        rating.save()
    else:
        Rating.objects.create(user=user, product=product, value=value)
    
    return Response('rating created', 201)