from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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
    actions = ('remove_cards',)

    @admin.display(ordering='cards_count')
    def cards_count(self, category):
        url = (
            reverse('admin:flash_card_flashcard_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            }))
        if category.cards_count == 1:
            return format_html('<a href="{}">{} card</a>', url, category.cards_count)
        elif category.cards_count == 0 or category.cards_count > 1:
            return format_html('<a href="{}">{} cards</a>', url, category.cards_count)
        

        return format_html('<a href="{}">{} cards</a>', url, category.cards_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            cards_count=Count('flashcard')
        )

    @admin.action(description='Remove Cards')
    def remove_cards(self, request, queryset):
        total_cards_count = sum(category.flashcard_set.count() for category in queryset)

        for category in queryset:
            category.flashcard_set.all().delete()

        self.message_user(
            request,
            f'{total_cards_count} cards were successfully removed',
            messages.SUCCESS
        )    




admin.site.unregister(User)
user = get_user_model()

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','is_staff','cards',)
    list_editable = ('is_staff',)
    list_filter = ('is_staff',CardsCountFilter)
    list_per_page = 10
    fields = ('username','password','first_name','last_name','email','is_staff','is_superuser',)
    search_fields = ('username',)

    @admin.display(ordering='cards')
    def cards(self, user):
        url = (
            reverse('admin:flash_card_flashcard_changelist')
            + '?'
            + urlencode({
                'user__id': str(user.id)
            }))
        if user.cards == 1:
            return format_html('<a href="{}">{} card</a>', url, user.cards)
        elif user.cards == 0 or user.cards > 1:
            return format_html('<a href="{}">{} cards</a>', url, user.cards)
        

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            cards=Count('flashcard')
        )

    