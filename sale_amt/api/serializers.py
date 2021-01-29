from rest_framework.serializers import ModelSerializer
from sale_amt.models import SaleAmount
from products.api.serializers import ProductSerializer

class SaleAmountSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SaleAmount
        fields = ('id', 'product', 'amount')