from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CondolenceView, ContactMessageView

post_router = DefaultRouter()
post_router.register(r'condolence', CondolenceView)
post_router.register(r'contactus', ContactMessageView)

urlpatterns = post_router.urls