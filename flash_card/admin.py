from django.contrib import admin
from .models import FlashCard, Category

# Register your models here.


@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title',)
    list_filter = ('category', 'user')
    list_editable = ('category',)
    list_per_page = 10
    autocomplete_fields = ('user', 'category',)
    search_fields = ('question',)
    list_select_related=('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
