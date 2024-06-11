# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Employee

@registry.register_document
class EmployeeDocument(Document):
    class Index:
        name = 'employees'

    class Django:
        model = Employee
        fields = [
            'emp_no',
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'hire_date',
        ]

