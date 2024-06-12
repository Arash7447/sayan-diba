
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, DeptManagerViewSet, DeptEmpViewSet, TitleViewSet, SalaryViewSet, employee_list
from . import views

router = DefaultRouter()

router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employee-list/', employee_list, name='employee-list'),
    path('employee-detail/<int:pk>/', views.employee_detail_html, name='employee-detail-html'),
    path('employee-update/<int:pk>/', views.employee_update_html, name='employee-update-html'),
    path('employee-delete/<int:pk>/', views.employee_delete_html, name='employee-delete-html'),
    
]
