from rest_framework import routers
from .views import FlashCardViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register('cards', FlashCardViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls
