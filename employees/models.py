from django.db import models

class Employee(models.Model):
    
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()

    class Meta:
        db_table = 'employees'
