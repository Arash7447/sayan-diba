from rest_framework import serializers
from .models import Employee, Department, DeptManager, DeptEmp, Title, Salary

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DeptManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeptManager
        fields = '__all__'

class DeptEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeptEmp
        fields = '__all__'

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
