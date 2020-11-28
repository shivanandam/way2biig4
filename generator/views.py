from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
    
def pwd(request):
    return render(request,'generator/pwd.html')
