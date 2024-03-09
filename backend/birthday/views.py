from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Birthday
from .serializers import BirthdaySerializer

class BirthdayView(ModelViewSet):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        birthday = get_object_or_404(Birthday, slug=slug)
        serializer = self.get_serializer(birthday)
        return response(serializer.data)
