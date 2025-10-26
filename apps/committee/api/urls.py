from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CommitteeMembersViewSet

committee_router = DefaultRouter()
committee_router.register(r'committee_members', CommitteeMembersViewSet)