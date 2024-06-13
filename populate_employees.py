import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sayan.settings')
django.setup()

from employees.models import Employee

fake = Faker()

def create_fake_employee(emp_no):
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = random.choice(['M', 'F'])
    hire_date = fake.date_between(start_date='-30y', end_date='today')

    return Employee(
        emp_no=emp_no,
        birth_date=birth_date,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        hire_date=hire_date
    )

def populate_employees(count):
    last_employee = Employee.objects.order_by('-emp_no').first()
    last_emp_no = last_employee.emp_no if last_employee else 0

    batch_size = 1000
    employees = []
    for i in range(count):
        emp_no = last_emp_no + 1 + i
        employee = create_fake_employee(emp_no)
        employees.append(employee)
        if (i + 1) % batch_size == 0:
            Employee.objects.bulk_create(employees)
            employees = []
            print(f'{i + 1} employees added.')
    if employees:
        Employee.objects.bulk_create(employees)
        print(f'{len(employees)} remaining employees added.')

if __name__ == '__main__':
    populate_employees(800000)
