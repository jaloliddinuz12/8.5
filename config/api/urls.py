from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, BookViewSet, CommentViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet)
router.register('books', BookViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
