from django.db import models

#ManyToMany relationship is a db relationship where you can associate multiple instances of one model of with multiple instances of another model
#Each MenuItem can be made up of multiple ingredients
#Each ingredient can used in multiple MenuItem's
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
            
class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    spicy_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'menu_menuitem'
        