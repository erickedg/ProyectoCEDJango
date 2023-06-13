from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeesSerializer
from employes.models import Employee


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()
