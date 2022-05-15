"""Define URL adress for learning_log"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Add defaulr URL adress
    path('', include('django.contrib.auth.urls')),
    # Registartion page
    path('register/', views.register, name='register'),
    
]


