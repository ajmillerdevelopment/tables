from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu(request):
    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})

def tables_index(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def table_detail(request, table_id):
    table = Table.objects.get(id=table_id)
    return render(request, 'table_detail.html', {'table': table})

def table_new(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TableForm()
        return render(request, 'table_new.html',{ 'form': form})

def table_close(request, table_id):
    table = Table.objects.get(id=table_id)
    return render(request, 'table_close.html', {'table': table})