from rest_framework.viewsets import ModelViewSet
from sale_amt.models import SaleAmount
from .serializers import SaleAmountSerializer

class SaleAmountViewSet(ModelViewSet):
    queryset = SaleAmount.objects.all()
    serializer_class = SaleAmountSerializer