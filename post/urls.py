from django.urls import include, path
from post.views import PostsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("posts", PostsViewSet, basename="posts")


urlpatterns = [
    path("", include(router.urls)),
]