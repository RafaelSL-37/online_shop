from rest_framework.serializers import ModelSerializer
from codes.models import Code

class CodeSerializer(ModelSerializer):
    class Meta:
        model = Code
        fields = ('id', 'code', 'promo_start', 'promo_end')