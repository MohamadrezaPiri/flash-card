from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import FlashCard
from .serializers import CreateFlashCardSerializer
# Create your views here.


class FlashCardViewSet(ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = CreateFlashCardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
