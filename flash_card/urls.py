from rest_framework import routers
from .views import FlashCardViewSet

router = routers.SimpleRouter()
router.register('cards', FlashCardViewSet)

urlpatterns = router.urls
