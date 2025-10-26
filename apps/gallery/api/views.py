from rest_framework.viewsets import ReadOnlyModelViewSet
from ..models import PhotoLink
from .serializers import PhotoLinkSerializer

class PhotoLinksViewSet(ReadOnlyModelViewSet):
    queryset = PhotoLink.objects.filter(is_visible=True).order_by('-date')  # Sort by date in descending order
    serializer_class = PhotoLinkSerializer