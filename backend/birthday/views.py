from rest_framework.viewsets import ModelViewSet
from .models import Birthday
from .serializers import BirthdaySerializer

class BirthdayView(ModelViewSet):
    queryset = Birthday.objects.all()
    serializer_class = BirthdaySerializer
    lookup_field = 'slug'
