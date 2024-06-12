from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render, get_object_or_404,redirect
from django_elasticsearch_dsl.registries import registry
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import EmployeeForm
from django.views import View


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



class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            employees = EmployeeDocument.search().query("multi_match", query=query, fields=['first_name', 'last_name'])
        else:
            employees = EmployeeDocument.search().all()
        return render(request, 'search_results.html', {'employees': employees})

class EmployeeListView(View):
    def get(self, request):
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

class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employees/employee_detail.html', {'employee': employee})

class EmployeeUpdateView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(instance=employee)
        return render(request, 'employees/employee_update.html', {'form': form})

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee-list')

class EmployeeDeleteView(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employees/employee_delete.html', {'employee': employee})

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect('employee-list')


class EmployeeCreateView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employees/employee_create.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
