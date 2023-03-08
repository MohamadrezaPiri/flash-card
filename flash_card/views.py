from rest_framework.viewsets import ModelViewSet
from .models import FlashCard
from .serializers import CreateFlashCardSerializer
# Create your views here.


class FlashCardViewSet(ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = CreateFlashCardSerializer
