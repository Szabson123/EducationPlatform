from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, DescriptionToArticleViewSet, ImageToArticleViewSet, CodeToArticleViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet)
router.register('descriptions', DescriptionToArticleViewSet)
router.register('images', ImageToArticleViewSet)
router.register('codes', CodeToArticleViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]