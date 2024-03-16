from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault, HiddenField
from post.models import Post

class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 1


class CreatePostSerializer(serializers.ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"
