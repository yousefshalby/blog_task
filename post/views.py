from post.models import Post
from post.permissions import CanEditOrDeletePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from post.serializers import CreatePostSerializer, PostsListSerializer


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all().select_related("author")
    permission_classes = [IsAuthenticated, CanEditOrDeletePermission]

    def get_serializer_class(self):
        if self.action == "list":
            return PostsListSerializer
        return super().get_serializer_class()