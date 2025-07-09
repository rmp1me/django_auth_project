from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required

def logout_me(request):
    logout(request)
    return redirect('home')

def home(request):
   return render(request,'home.html')

def login_me(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # now refers to django.contrib.auth.login
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'].strip()
        last_name = request.POST['last_name'].strip()
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, "User registered successfully.")
        return redirect('home')

    return render(request, 'register.html')

def check_username_email(request):
    username = request.GET.get('username')
    email = request.GET.get('email')

    data = {
        'username_exists': User.objects.filter(username=username).exists() if username else False,
        'email_exists': User.objects.filter(email=email).exists() if email else False,
    }
    return JsonResponse(data)

