from django.contrib import admin

# name of the model from models.py
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

# goes into django admin site, + add 2nd param 
admin.site.register(Realtor, RealtorAdmin)
