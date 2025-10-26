from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PhotoLinksViewSet

PhotoLink_router = DefaultRouter()
PhotoLink_router.register(r'photo_links', PhotoLinksViewSet)