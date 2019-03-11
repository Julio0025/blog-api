from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from pyphonetics import Soundex

from post.functions import soundex_filter
from post.permissions import PostPermissions
from post.serializers import PostListSerializer, PostDetailSerializer, PostCreateEditSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    permission_classes = (PostPermissions, )
    queryset = Post.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            return PostDetailSerializer
        elif self.action in ['create', 'update']:
            return PostCreateEditSerializer
        return PostListSerializer


@api_view(['GET'])
def soundex_search(request, pk, keyword):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'Status': 'Post does not exist'})

    matched_words = soundex_filter(post.content, keyword)
    return Response({'matched_words': matched_words})





