from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from .serializers import PostSerializer
from .permissoins import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    # lookup_field = 'first_name' para buscar por first name en lugar de id
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']
    filterset_fields = ['category__slug', 'category']  # se puede colocar cuantos campos necesarios para filtrar segun
