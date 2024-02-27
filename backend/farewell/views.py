from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Condolence, ContactMessage
from .serializers import CondolenceSerializer, ContactMessageSerializer

# Create your views here.
class CondolenceView(ModelViewSet):
    queryset = Condolence.objects.all()
    serializer_class = CondolenceSerializer

class ContactMessageView(ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
