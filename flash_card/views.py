from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FlashCardFilters
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .models import FlashCard, Category
from .serializers import FlashCardSerializer, CreateFlashCardSerializer, UpdateFlashCardSerializer, CategorySerializer
# Create your views here.


class FlashCardViewSet(ModelViewSet):
    queryset = FlashCard.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = FlashCardFilters
    pagination_class = PageNumberPagination
    search_fields = ('question',)
    ordering_fields = ('created_at',)

    def get_serializer_class(self):
        method = self.request.method

        if method == 'POST':
            return CreateFlashCardSerializer
        elif method == 'PUT':
            return UpdateFlashCardSerializer
        return FlashCardSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
