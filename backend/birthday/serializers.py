from rest_framework.serializers import ModelSerializer
from .models import Birthday

class BirthdaySerializer(ModelSerializer):
    class Meta:
        model = Birthday
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'image', 'slug')
