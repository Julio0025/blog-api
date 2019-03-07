from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CurrentUserDefault
from post.models import Post
import datetime


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        return Post.objects.get(instance).update(
            edited=datetime.datetime.now(),
            title=validated_data.title,
            content=validated_data.content)



