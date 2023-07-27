from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('get_table/', views.get_table, name='get_table'),
    path('get_menu/', views.get_menu, name='get_menu'),
]