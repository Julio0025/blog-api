from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.utils import timezone

from post.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'created')


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()

    @staticmethod
    def get_user(obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = ('title', 'content', 'created', 'edited', 'user')


class PostCreateEditSerializer(ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.edited = timezone.now()
        instance.save()
        return instance

    class Meta:
        model = Post
        fields = ('title', 'content')





