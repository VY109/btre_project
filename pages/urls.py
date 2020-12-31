from django.urls import path

# from all import views
from  . import views 

# path is '' nothing -- root path, the home page
# 1. then the method(index) we want to connect to in the view = index, then the name to easily access the view
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]


