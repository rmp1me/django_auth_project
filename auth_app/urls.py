from django.urls import path
from .views import home, register

urlpatterns = [
    path('', home, name='home'), 
    path('register/', register, name='register'),  # Assuming register view is same as home for now
]