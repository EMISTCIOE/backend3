from rest_framework.serializers import ModelSerializer
from ..models import Member

class CommitteeSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('sno', 'name', 'position', 'batch', 'image')