# BACKEND BISTRO

## MoSCoW
## Must haves
`
1. Database Schema:
    - Menu Items:
        - Title (CharField)
        - Description (TextField)
        - Price (DecimalField)
        - Spiciness (IntegerField)
        - Category (ForeignKey to 'Category' model)
        - Cuisine (ForeignKey to 'Cuisine' model)
    - Category:
        - Id (IntegerField)
    - Cuisine:
        - Id (Integerfield)

2. Views
    - 
`
## Should haves
`
1. Testing - Tests for models and views?
2. Error Messaging - Handle backend errors and provide error messaging
3. 
`
## Could haves
`
1. Search
2. Filter
3. CSV export of data with new route DONE

`


## CRUD
`
1. Create new menu items
    - Request data from JSON: title, description, price, spiciness, category, cuisine details

2. Read menu items

3. Update menu items

4. Delete menu items
`

## INIT
## Models.py
`
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    spicy_level = models.IntegerField()
    category = models.ForeignKey
    cuisine = models.ForeignKey

    def __str__(self):
        return self.title
`

## views.py

"Views in Django are Python functions or classes that handle incoming HTTP requests and return HTTP responses."
`
from django.http import JsonResponse
from .models import MenuItem

def full_menu(request):
    menu = MenuItem.objects.all()
    data = []
    for item in menu:
        data.append({
            'id':item.id,
            'title':item.title,
            'description':item.description,
            'price': item.price,
            'spicy_level': item.spicy_level,
            'category': item.category.name,
            'cuisine': item.cuisine.name,            
        })
    return JsonResponse(data)
`

## urls.py
`
from django.urls import path
from .views import full_menu

urlpatterns = [
    path('/menu-items/', full_menu, name = 'full_menu'),
]
`