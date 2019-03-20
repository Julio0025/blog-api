from django.conf.urls import url
from rest_framework import routers

from post import views


router = routers.SimpleRouter()

router.register(r'post', views.PostViewSet, base_name='post')

urlpatterns = router.urls
