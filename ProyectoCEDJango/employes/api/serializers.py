from rest_framework import serializers
from employes.models import Employee


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'charge']
