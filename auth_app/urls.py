from django.urls import path
from .views import home, register, login_me

urlpatterns = [
    path('', home, name='home'), 
    path('register/', register, name='register'), 
    path('login/',login_me,name='login')
]