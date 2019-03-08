from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.permissions import PostPermissions
from post.serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (PostPermissions, )
    queryset = Post.objects.all()






