from rest_framework import routers
from .views import PostViewSet

router = routers.SimpleRouter()

router.register(r'post', PostViewSet, base_name='')

urlpatterns = router.urls
