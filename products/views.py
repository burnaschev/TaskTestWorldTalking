from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Recipe, RecipeIngredient, Product


@transaction.atomic
def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)

    recipe_ingredient, created = RecipeIngredient.objects.get_or_create(recipe=recipe, product=product)

    if not created:
        recipe_ingredient.weight_in_grams = weight
        recipe_ingredient.save()

    return JsonResponse({'status': 'success'})


@transaction.atomic
def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = recipe.recipeingredient_set.all()

    for ingredient in ingredients:
        ingredient.product.times_used += 1

    Product.objects.bulk_update([ingredient.product for ingredient in ingredients], ['times_used'])

    return JsonResponse({'status': 'success'})


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    recipes = Recipe.objects.filter(
        ~Q(recipeingredients__product=product) |
        Q(recipeingredients__product=product, recipeingredients__weight_in_grams__lt=10)
    ).distinct()

    context = {
        'recipes': recipes,
        'product': product,
    }

    return render(request, 'products/recipes_without_product.html', context)
