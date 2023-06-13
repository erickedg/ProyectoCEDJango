from rest_framework.viewsets import ModelViewSet
from ..models import Comment
from .serializers import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backend = [OrderingFilter]
    filter_backends = [DjangoFilterBackend, DjangoFilterBackend]
    filterset_fields = ['post', 'post__slug']
    ordering = ['-created_at']
