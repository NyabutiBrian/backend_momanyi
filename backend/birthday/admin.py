from django.contrib import admin
from .models import Birthday

# CHANGING TABLE LAYOUT
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'slug')
    list_filter = ['birth_date']

# Register your models here.
admin.site.register(Birthday, BirthdayAdmin)