from django.contrib import admin
from .models import Condolence, ContactMessage

# CHANGING TABLE LAYOUT
class CondolenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'message', 'message_date')
    list_filter = ['message_date']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'message', 'message_date')
    list_filter = ['message_date']

# Register your models here.
admin.site.register(Condolence, CondolenceAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)