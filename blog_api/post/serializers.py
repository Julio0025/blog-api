from rest_framework.serializers import ModelSerializer
from django.utils import timezone

from post.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.edited = timezone.now()
        instance.save()
        return instance



