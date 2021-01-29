from rest_framework.viewsets import ModelViewSet
from used_codes.models import UsedCode
from .serializers import UsedCodeSerializer

class UsedCodesViewSet(ModelViewSet):
    queryset = UsedCode.objects.all()
    serializer_class = UsedCodeSerializer