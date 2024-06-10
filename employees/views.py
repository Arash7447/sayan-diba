from django.shortcuts import render
from .search_indexes import EmployeeDocument
from rest_framework import viewsets
from .models import Employee, Department, DeptManager, DeptEmp, Title, Salary
from .serializers import EmployeeSerializer, DepartmentSerializer, DeptManagerSerializer, DeptEmpSerializer, TitleSerializer, SalarySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeptManagerViewSet(viewsets.ModelViewSet):
    queryset = DeptManager.objects.all()
    serializer_class = DeptManagerSerializer

class DeptEmpViewSet(viewsets.ModelViewSet):
    queryset = DeptEmp.objects.all()
    serializer_class = DeptEmpSerializer

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

def search(request):
    query = request.GET.get('q')
    if query:
        employees = EmployeeDocument.search().query("multi_match", query=query, fields=['first_name', 'last_name', 'department'])
    else:
        employees = EmployeeDocument.search().all()
    
    return render(request, 'search_results.html', {'employees': employees})
