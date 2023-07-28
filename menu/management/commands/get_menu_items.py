from django.core.management.base import BaseCommand
from menu.views import add_menu_items_to_database

class Command(BaseCommand):
    help = 'Add menu items and their associated ingredients to the database.'

    def handle(self, *args, **kwargs):
        add_menu_items_to_database(None)
        self.stdout.write(self.style.SUCCESS('Menu items added successfully.'))
