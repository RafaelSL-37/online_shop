from rest_framework.viewsets import ModelViewSet
from products.models import Product
from .serializers import ProductSerializer
from .serializers import ProductLiteSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductLiteViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductLiteSerializer