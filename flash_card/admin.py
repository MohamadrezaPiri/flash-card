from django.contrib import admin
from django.urls import reverse
from django.utils.html import urlencode,format_html
from django.db.models.aggregates import Count
from .models import FlashCard, Category
from .filters import CardsCountFilter

# Register your models here.


@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title','last_update')
    list_filter = ('category__name','user__username')
    list_editable = ('category',)
    list_per_page = 10
    autocomplete_fields = ('user', 'category',)
    search_fields = ('question','user__username')
    list_select_related=('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','cards_count',)
    list_filter = (CardsCountFilter,)
    list_per_page = 10
    search_fields = ('name',)

    @admin.display(ordering='cards_count')
    def cards_count(self, category):
        url = (
            reverse('admin:flash_card_flashcard_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            }))
        return format_html('<a href="{}">{} cards</a>', url, category.cards_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            cards_count=Count('flashcard')
        )


