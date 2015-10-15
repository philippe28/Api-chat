from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import url, include


router = DefaultRouter()
router.register(r'chat', views.ChatViewSet)