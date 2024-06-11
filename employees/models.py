# models.py

from django.db import models

class Department(models.Model):
    dept_no = models.CharField(max_length=4, primary_key=True)
    dept_name = models.CharField(max_length=40)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    emp_no = models.AutoField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    hire_date = models.DateField()

    class Meta:
        db_table = 'employees'

class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f'{self.emp_no} - {self.dept_no}'

class DeptManager(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f'{self.emp_no} - {self.dept_no}'

class Salary(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f'{self.emp_no} - {self.salary}'

class Title(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return f'{self.emp_no} - {self.title}'
