from django.shortcuts import render,HttpResponse

def home(request):
   return render(request,'home.html')
def register(request):
   return render(request,'register.html')
