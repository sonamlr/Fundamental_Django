from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def main_app(request):
    return render(request, 'main/main.html')