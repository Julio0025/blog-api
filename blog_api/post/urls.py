from django.conf.urls import url
from rest_framework import routers

from post import views


router = routers.SimpleRouter()

router.register(r'post', views.PostViewSet, base_name='post')

urlpatterns = [
    url(r'post/(?P<pk>\d+)/(?P<keyword>[\w-]+)/', views.soundex_search)
]

urlpatterns += router.urls
