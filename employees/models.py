from django.db import models

class Employee(models.Model):
    emp_no = models.AutoField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    hire_date = models.DateField()

    class Meta:
        db_table = 'employees'

    def save(self, *args, **kwargs):
        if not self.emp_no:
            last_employee = Employee.objects.order_by('-emp_no').first()
            if last_employee:
                self.emp_no = last_employee.emp_no + 1
            else:
                self.emp_no = 1
        super().save(*args, **kwargs)

