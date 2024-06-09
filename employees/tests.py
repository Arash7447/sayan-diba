from django.test import TestCase
from .models import Employee
from django.urls import reverse

class EmployeeModelTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            emp_no=1,
            first_name='John',
            last_name='Doe',
            gender='M',
            birth_date='1990-01-01',
            hire_date='2020-01-01'
        )

    def test_create_employee(self):
        self.assertEqual(self.employee.first_name, 'John')

    def test_read_employee(self):
        employee = Employee.objects.get(emp_no=1)
        self.assertEqual(employee.first_name, 'John')

    def test_update_employee(self):
        self.employee.first_name = 'Jane'
        self.employee.save()
        self.assertEqual(self.employee.first_name, 'Jane')

    def test_delete_employee(self):
        self.employee.delete()
        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(emp_no=1)

class EmployeeViewTests(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            emp_no=1,
            first_name='John',
            last_name='Doe',
            gender='M',
            birth_date='1990-01-01',
            hire_date='2020-01-01'
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John')

    def test_employee_create_view(self):
        response = self.client.post(reverse('employee_create'), {
            'emp_no': 2,
            'first_name': 'Jane',
            'last_name': 'Doe',
            'gender': 'F',
            'birth_date': '1991-01-01',
            'hire_date': '2021-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 2)

    def test_employee_update_view(self):
        response = self.client.post(reverse('employee_update', args=[self.employee.pk]), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'gender': 'F',
            'birth_date': '1990-01-01',
            'hire_date': '2020-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, 'Jane')

    def test_employee_delete_view(self):
        response = self.client.post(reverse('employee_delete', args=[self.employee.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Employee.objects.count(), 0)

