from django_filters.rest_framework import FilterSet
from .models import FlashCard


class FlashCardFilters(FilterSet):
    class Meta:
        model = FlashCard
        fields = {
            'category_id': ['exact']
        }
