from rest_framework.viewsets import ModelViewSet
from codes.models import Code
from .serializers import CodeSerializer

class CodeViewSet(ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer