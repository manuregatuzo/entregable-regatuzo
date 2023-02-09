from django.urls import path
from products.views import create_products, list_products



urlpatterns = [
    path('create-product/', create_products),
    path('list-product/', list_products),

]