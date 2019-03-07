from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def list(self, request):
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Post.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = PostSerializer(user)
    #     return Response(serializer.data)
