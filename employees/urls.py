from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, DeptManagerViewSet, DeptEmpViewSet, TitleViewSet, SalaryViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'deptmanagers', DeptManagerViewSet)
router.register(r'deptemps', DeptEmpViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'salaries', SalaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
