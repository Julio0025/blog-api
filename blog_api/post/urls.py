from django.conf.urls import url
from rest_framework import routers

from post import views
from .views import PostViewSet

router = routers.SimpleRouter()

router.register(r'post', views.PostViewSet, )

urlpatterns = [
    url(r'post/(?P<pk>\d+)/(?P<keyword>[\w-]+)/', views.soundex_search)
]

urlpatterns += router.urls
