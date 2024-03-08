from rest_framework.routers import DefaultRouter
from posts.api.view import PostModelViewSet

router_post = DefaultRouter()

router_post.register(prefix='posts', viewset=PostModelViewSet, basename='posts')