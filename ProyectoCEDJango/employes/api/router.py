from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet


router_employees = DefaultRouter()

router_employees.register(prefix='employees', basename='employees', viewset=EmployeeViewSet)
