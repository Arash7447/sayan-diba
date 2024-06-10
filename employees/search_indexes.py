from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Employee, Department

@registry.register_document
class EmployeeDocument(Document):
    department = fields.ObjectField(properties={
        'dept_name': fields.TextField()
    })

    class Index:
        name = 'employees'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Employee
        fields = [
            'emp_no',
            'birth_date',
            'first_name',
            'last_name',
            'gender',
            'hire_date',
            'salary',
        ]
        related_models = [Department]
