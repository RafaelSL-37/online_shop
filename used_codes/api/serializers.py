from rest_framework.serializers import ModelSerializer
from used_codes.models import UsedCode

class UsedCodeSerializer(ModelSerializer):
    class Meta:
        model = UsedCode
        fields = ('id', 'code', 'user', 'use')