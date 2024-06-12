from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employee, Department, DeptEmp, DeptManager, Salary, Title
from .serializers import EmployeeSerializer, DepartmentSerializer, DeptEmpSerializer, DeptManagerSerializer, SalarySerializer, TitleSerializer
from django.shortcuts import render, get_object_or_404,redirect
from django_elasticsearch_dsl.registries import registry
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    employee_objects = Employee.objects.all()
    paginator = Paginator(employee_objects, 10)  
    page_number = request.GET.get('page')
    
    try:
        employees = paginator.get_page(page_number)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


def employee_update_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-detail-html', pk=pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_update.html', {'form': form})


def employee_delete_html(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee-list')  
    return render(request, 'employees/employee_delete.html', {'employee': employee})