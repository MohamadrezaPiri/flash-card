from django.contrib import admin
from .models import FlashCard, Category

# Register your models here.


@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
