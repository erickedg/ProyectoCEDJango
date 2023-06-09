from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
