from django.urls import path
from products.views import create_products, list_products, list_categories, create_category


urlpatterns = [
    path('create-product/', create_products),
    path('list-product/', list_products),
    path('list-categories/' , list_categories),
    path('crear-cat/',create_category),
]