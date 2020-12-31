"""
1. python manage.py startapp accounts
2. add new 'accounts' folder in 'templates'
    2a. add new html files
3. in btre projects folder 
    - settings.py; add 'accounts' to installed apps section
    - urls.py; add 'accounts/' to url pattern
4. add 'urls.py' here, dj doesn't create this with 'startapp' 


"""
from django.urls import path

# from all import views
from  . import views 

# 4 different urls
# login, views method/function 'login', name login
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
