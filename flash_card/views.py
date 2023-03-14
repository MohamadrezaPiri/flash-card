from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .models import FlashCard, Category
from .serializers import CreateFlashCardSerializer, CategorySerializer
# Create your views here.


class FlashCardViewSet(ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = CreateFlashCardSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('question',)
    ordering_fields = ('created_at',)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
