from django.contrib import admin

from products.models import Product, Recipe, RecipeIngredient


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    fields = ['product', 'weight_in_grams']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RecipeIngredientInline]
