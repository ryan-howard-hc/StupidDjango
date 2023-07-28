from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.http import JsonResponse
from .models import MenuItem

def default_menu(request):
    return redirect('get_menu')

def get_table(request):
    getit = list(MenuItem.objects.values())
    return JsonResponse({'data': getit})

def get_menu(request):
    menu_items = MenuItem.objects.select_related().all()
    data = []

    for item in menu_items:
        data.append({
            'title': item.title,
            'description': item.description,
            'price': float(item.price), 
            'spicy_level': item.spicy_level,
            'category': item.category.name,
            'cuisine': item.cuisine.name, 
        })

    return JsonResponse(data, safe=False)