from rest_framework import mixins

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ProductSerializer
from .models import Category, Product

class CategoryViewSet(mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin, 
                     mixins.ListModelMixin, 
                     GenericViewSet):

    queryset = Category.objects.all()


class ProductViewSet(ModelViewSet,mixins.ListModelMixin,GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

