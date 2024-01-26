from django.urls import path

from products.apps import ProductsConfig
from products.views import show_recipes_without_product

app_name = ProductsConfig.name


urlpatterns = [
    path('recipe/<int:product_id>', show_recipes_without_product, name='recipe-private')
]
