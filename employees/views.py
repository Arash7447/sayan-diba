from rest_framework import viewsets
from .models import Employee, Department, DeptEmp, DeptManager, Salary, Title
from .serializers import EmployeeSerializer, DepartmentSerializer, DeptEmpSerializer, DeptManagerSerializer, SalarySerializer, TitleSerializer
from django.shortcuts import render
from django_elasticsearch_dsl.registries import registry

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeptEmpViewSet(viewsets.ModelViewSet):
    queryset = DeptEmp.objects.all()
    serializer_class = DeptEmpSerializer

class DeptManagerViewSet(viewsets.ModelViewSet):
    queryset = DeptManager.objects.all()
    serializer_class = DeptManagerSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

def search(request):
    query = request.GET.get('q')
    if query:
        employees = EmployeeDocument.search().query("multi_match", query=query, fields=['first_name', 'last_name'])
    else:
        employees = EmployeeDocument.search().all()
    
    return render(request, 'search_results.html', {'employees': employees})

def employee_list(request):
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 10)  
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)
    return render(request, 'employees/employee_list.html', {'employees': employees})