# Generated by Django 5.0.2 on 2024-06-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=1)),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]