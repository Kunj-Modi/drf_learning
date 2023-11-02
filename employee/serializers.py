from rest_framework import serializers

from .models import Department, Employee


class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'dep_id',
            'dep_name',
        ]


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'emp_id',
            'emp_name',
            'emp_dep',
        ]
