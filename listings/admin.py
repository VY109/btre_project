from django.contrib import admin

# name of the model from models.py
from .models import Listing

# adding extra 'fields' in listing for the admin area, 
# also need to pass in the listingAdmin class in the admin.site.register
# make the 'title' clickable and also keep the id (the first one)
# + add filter for realtor, for having 1 value add a comma , 
class listingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price','list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable= ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

# goes into django admin site
admin.site.register(Listing, listingAdmin)
