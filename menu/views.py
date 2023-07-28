from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from django.http import JsonResponse, HttpResponse
from .models import MenuItem, Category, Cuisine, Ingredient
import json
import csv

def default_menu(request):
    return redirect('get_menu')

def get_table(request):
    getit = list(MenuItem.objects.values())
    return JsonResponse({'data': getit})

def get_menu(request):
    menu_items = MenuItem.objects.select_related().all()
    data = []

    for item in menu_items:
        ingredients_list = [ingredient.name for ingredient in item.ingredients.all()]

        data.append({
            'title': item.title,
            'description': item.description,
            'price': float(item.price), 
            'spicy_level': item.spicy_level,
            'category': item.category.name,
            'cuisine': item.cuisine.name, 
            'ingredients': ingredients_list, 
        })

    return JsonResponse(data, safe=False)


def add_menu_items_to_database(request):
    json_data = '''{
        "ingredients": [
    {
      "name": "Mud"
    },
    {
      "name": "Lobsters"
    },
    {
      "name": "Monkey Brain"
    },
    ...
  ],
      
  "menuItems": [
    {
      "id": 9,
      "name": "Butterbeer",
      "price": "$5.00",
      "description": "Butterbeer",
      "spicy_level": 0,
      "category": 1,
      "cuisine": 1
    },
    {
      "id": 10,
      "name": "Pumpkin Pasties",
      "price": "$3.00",
      "description": "Spiced pumpkin filling.",
      "spicy_level": 0,
      "category": 3,
      "cuisine": 2
    },
    {
      "id": 11,
      "name": "Bertie Bott's Every Flavor Beans",
      "price": "$2.00",
      "description": "A box of magical jelly beans with surprising and unpredictable flavors.",
      "spicy_level": 0,
      "category": 2,
      "cuisine": 3
    },
    {
      "id": 12,
      "name": "Chocolate Frogs",
      "price": "$4.00",
      "description": "Chocolates shaped like frogs that will run away in fear",
      "spicy_level": 0,
      "category": 1,
      "cuisine": 4
    },
    {
      "id": 13,
      "name": "Treacle Tart",
      "price": "$6.00",
      "description": "Tart made with golden syrup and breadcrumbs.",
      "spicy_level": 0,
      "category": 3,
      "cuisine": 5
    },
    {
      "id": 14,
      "name": "Polyjuice Potion",
      "price": "$8.00",
      "description": "Allows the drinker to assume the appearance of another person.",
      "spicy_level": 0,
      "category": 4,
      "cuisine": 6
    },
    {
      "id": 15,
      "name": "Cauldron Cakes",
      "price": "$3.00",
      "description": "Chocolate cupcakes",
      "spicy_level": 0,
      "category": 2,
      "cuisine": 1
    },
    {
      "id": 16,
      "name": "Mandrake Cakes",
      "price": "$4.00",
      "description": "Magical cakes of mandrake plants.",
      "spicy_level": 0,
      "category": 1,
      "cuisine": 2
    },
    {
      "id": 17,
      "name": "Hagrid's Rock Cakes",
      "price": "$4.00",
      "description": "Homemade cakes baked by Hagrid",
      "spicy_level": 0,
      "category": 3,
      "cuisine": 3
    },
    {
      "id": 18,
      "name": "Pumpkin Juice",
      "price": "$3.00",
      "description": "Freshly squeezed pumpkins",
      "spicy_level": 0,
      "category": 2,
      "cuisine": 4
    },
    {
      "id": 19,
      "name": "Chocolate Cauldrons",
      "price": "$5.00",
      "description": "Chocolate shaped like cauldrons, filled with molten caramel",
      "spicy_level": 0,
      "category": 1,
      "cuisine": 5
    },
    {
      "id": 20,
      "name": "Fizzing Whizzbees",
      "price": "$4.00",
      "description": "Fizzing candies that create a magical and explosive sensation in your mouth.",
      "spicy_level": 0,
      "category": 4,
      "cuisine": 6
    },
    {
      "id": 21,
      "name": "Honeydukes Chocolate",
      "price": "$6.00",
      "description": "Honeydukes sweet shop homemade chocolate",
      "spicy_level": 0,
      "category": 2,
      "cuisine": 1
    }
  ]
}
'''

    data = json.loads(json_data)
    ingredients = data["ingredients"]
    for ingredient_data in ingredients:
        ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_data["name"])

    menu_items = data["menuItems"]

    for item in menu_items:
        
        category, _ = Category.objects.get_or_create(name=item["category"])
        cuisine, _ = Cuisine.objects.get_or_create(name=item["cuisine"])

        menu_item = MenuItem(
            title=item["name"],
            description=item["description"],
            price=float(item["price"].replace("$", "")),
            spicy_level=item["spicy_level"],
            category=category,
            cuisine=cuisine,
        )

        menu_item.save()
        for ingredient_id in item["ingredients"]:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            menu_item.ingredients.add(ingredient)
    return JsonResponse({"message": "Menu items added successfully."})
  
def export_menu_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="menu_items.csv"' #this is largely for user-end experience, though it's also for consistency across all browser defaults
                                                                                #Not totally necessary though
    
    menu_items = MenuItem.objects.all()  #simply fetches all the menuitems from the db table

    writer = csv.writer(response)       #writer is just a variable, but it uses csv.writer to write the csv data into the httpresponse as an argument
    writer.writerow(['Title', 'Description', 'Price', 'Spicy Level', 'Category', 'Cuisine']) 

    for item in menu_items:
        writer.writerow([item.title, item.description, item.price, item.spicy_level, item.category.name, item.cuisine.name])

    return response