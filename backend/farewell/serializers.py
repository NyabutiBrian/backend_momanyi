from rest_framework.serializers import ModelSerializer
from .models import Condolence, ContactMessage

class CondolenceSerializer(ModelSerializer):
    class Meta:
        model = Condolence
        fields = ('id', 'full_name', 'message', 'message_date')

class ContactMessageSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ('id', 'full_name', 'email', 'message', 'message_date')
