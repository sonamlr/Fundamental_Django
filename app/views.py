from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def main_app(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'main/main.html', {"chais":chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'main/chai_detail.html', {"chai":chai})