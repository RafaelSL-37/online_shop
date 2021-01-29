from rest_framework.serializers import ModelSerializer
from sales.models import Sale
from sale_amt.api.serializers import SaleAmountSerializer

class SaleSerializer(ModelSerializer):
    sale_amount = SaleAmountSerializer(many=True)

    class Meta:
        model = Sale
        fields = ('id', 'user', 'sale_amount', 'date', 'approval')