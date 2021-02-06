from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def menu(request):
    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})
def covers_index(request):
    covers = Cover.objects.all()
    return render(request, 'covers_index.html', {'covers': covers})
def cover_detail(request, cover_id):
    cover = Cover.objects.get(id=cover_id)
    return render(request, 'cover_detail.html', {'cover': cover})
def cover_new(request):
    return render(request, 'cover_new.html')
def cover_close(request, cover_id):
    cover = Cover.objects.get(id=cover_id)
    return render(request, 'cover_close.html', {'cover': cover})