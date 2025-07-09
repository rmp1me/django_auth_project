from django.urls import path
from .views import home, register, login_me
from .views import home, register, login_me, logout_me,check_username_email

urlpatterns = [
    path('', home, name='home'), 
    path('register/', register, name='register'), 
    path('login/',login_me,name='login'),
    path('logout/', logout_me, name='logout'),
    path('check-user/', check_username_email, name='check_user'),
]