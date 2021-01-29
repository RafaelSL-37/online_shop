from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'ratings', 'image')
        #FAZER SEGUNDO SERIALIZAR MENOR PRA VITRINE

class ProductLiteSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image')