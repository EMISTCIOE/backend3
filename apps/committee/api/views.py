from rest_framework.viewsets import ReadOnlyModelViewSet
from ..models import Member
from .serializers import CommitteeSerializer

class CommitteeMembersViewSet(ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = CommitteeSerializer