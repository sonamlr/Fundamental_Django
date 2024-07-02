from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm
from .models import ChaiVarity, Store
# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def main_app(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'main/main.html', {"chais":chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'main/chai_detail.html', {"chai":chai})


def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.changed_data['chai_variety']
            stores = Store.objects.filter(chai_varieties = chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request, 'chai/chai_store.html', {'stores':stores, 'form':form})

