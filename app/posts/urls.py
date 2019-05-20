from rest_framework.routers import SimpleRouter
from .viewsets import PostViewSet


router = SimpleRouter(trailing_slash=True)
router.register(r'', PostViewSet)

urlpatterns = router.urls
