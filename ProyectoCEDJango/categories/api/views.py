from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(published=False) #Para regresar registros qque cumplan con filtros establecidos aqui
    lookup_field = 'slug' #  buscara por esta propiedad
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published'] #  para que se registre en insomnia, se consume el endpoint /?[filtersetr_field]=''
