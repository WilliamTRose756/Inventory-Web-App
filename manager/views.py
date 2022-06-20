from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime




def manager(request):
    items = Item.objects.all()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager')
    else:
        form = ItemForm()

    context = {
        'items':items,
        'form': form,
    }

    return render(request, 'index.html', context)


def item_delete(request, pk):
    selected = Item.objects.get(id=pk) 
    if request.method == 'POST':
        selected.delete()
        return redirect('manager')
    return render(request, 'delete.html')


def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('manager')
    else:
        form = ItemForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Item.objects.filter(Q(lot_number__contains=searched) | Q(item_name__contains=searched) | Q(exp_date__contains=searched))
        return render(request, 'search_results.html',
        {'searched':searched,
        'results':results},)
    else:
        return render(request, 'search_results.html')


def expiration(request):
    if request.method == 'GET':
        expirations = Item.objects.filter(exp_date__lte=datetime.now())
        return render(request, 'expiration.html', 
        {'expirations': expirations})


def logout_user(request):
    logout(request)
    return redirect('login.html')

















    
    


