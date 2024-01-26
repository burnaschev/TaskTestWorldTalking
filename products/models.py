from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='название')
    times_used = models.IntegerField(default=0, verbose_name='продукт был использован')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    ingredients = models.ManyToManyField(Product, through='RecipeIngredient', verbose_name='ингредиенты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='рецепт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    weight_in_grams = models.IntegerField(verbose_name='вес гр')

    def __str__(self):
        return f"{self.product.name} - {self.weight_in_grams}g"

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        unique_together = ('recipe', 'product')
