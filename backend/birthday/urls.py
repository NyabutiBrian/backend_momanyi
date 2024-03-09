from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BirthdayView

post_router = DefaultRouter()
post_router.register(r'details', BirthdayView)
post_router.register(r'<slug:slug>', BirthdayView)

urlpatterns = post_router.urls