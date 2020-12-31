from django.urls import path

# from all import views
from  . import views 

# path is '' nothing -- root path, the home page but in here is /listings
# from '', views.py calls the .index method
# /listings/23..
# in views.py create methods for index, listing and search
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
