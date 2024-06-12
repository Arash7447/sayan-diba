from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeListView, EmployeeDetailView, EmployeeUpdateView, EmployeeDeleteView, EmployeeCreateView, EmployeeViewSet

router = DefaultRouter()

router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employee-list/', EmployeeListView.as_view(), name='employee-list'),
    path('employee-detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail-html'),
    path('employee-update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update-html'),
    path('employee-delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete-html'),
    path('employee-create/', EmployeeCreateView.as_view(), name='employee-create-html'),
]