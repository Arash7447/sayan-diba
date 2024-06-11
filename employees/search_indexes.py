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
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'salary',
        ]
        related_models = [Department]

    def get_queryset(self):
        return super(EmployeeDocument, self).get_queryset().select_related('department')

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Department):
            return related_instance.employee_set.all()
