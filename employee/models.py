from django.db import models


class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dep_name}"


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    emp_dep = models.ForeignKey(to=Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.emp_id} {self.emp_name} {self.emp_dep}"
