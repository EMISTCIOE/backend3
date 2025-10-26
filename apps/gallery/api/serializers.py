from rest_framework.serializers import ModelSerializer
from ..models import PhotoLink

class PhotoLinkSerializer(ModelSerializer):
    class Meta:
        model = PhotoLink
        fields = ('id', 'title', 'url', 'date')