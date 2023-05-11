from django_filters.rest_framework import FilterSet
from django.db.models import Count
from django.contrib import admin
from .models import FlashCard


class FlashCardFilters(FilterSet):
    class Meta:
        model = FlashCard
        fields = {
            'category_id': ['exact']
        }


class CardsCountFilter(admin.SimpleListFilter):
    title = 'Cards count'
    parameter_name = 'FlashCard_set'

    def lookups(self, request, model_admin):
        return [
            ('<1','Without Card'),
            ('0<','With Card')
        ]
    
    def queryset(self, request, queryset):
        annotated_value = queryset.annotate(cards_count = Count('flashcard'))
        if self.value() == '<1':
            return annotated_value.filter(cards_count__lt=1)
        elif self.value() == '0<':
            return annotated_value.filter(cards_count__gt=0)