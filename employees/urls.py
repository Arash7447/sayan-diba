
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, DeptEmpViewSet, DeptManagerViewSet, SalaryViewSet, TitleViewSet, search, employee_list

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'deptemps', DeptEmpViewSet)
router.register(r'deptmanagers', DeptManagerViewSet)
router.register(r'salaries', SalaryViewSet)
router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('search/', search, name='search'),
    path('employees/', employee_list, name='employee_list'),
]