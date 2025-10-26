from rest_framework.routers import DefaultRouter
from committee.api.urls import committee_router
from gallery.api.urls import PhotoLink_router
from django.urls import path, include

router = DefaultRouter()
#committee_members
router.registry.extend(committee_router.registry)

#photo_links
router.registry.extend(PhotoLink_router.registry)

urlpatterns = [
     path('', include(router.urls))
]
