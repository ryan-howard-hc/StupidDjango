from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_menu, name='default_menu'),
    path('get_table/', views.get_table, name='get_table'),
    path('get_menu/', views.get_menu, name='get_menu'),
]