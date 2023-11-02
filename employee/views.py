from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import Department, Employee
from .serializers import DepSerializer, EmpSerializer


class EmpCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer

    def perform_create(self, serializer):
        emp_id = serializer.validated_data.get('emp_id')
        emp_name = serializer.validated_data.get('emp_name')
        emp_dep = serializer.validated_data.get('emp_dep')
        emp_des = serializer.validated_data.get('emp_des') or None
        if emp_des is None:
            emp_des = f"{emp_id} {emp_name} {emp_dep}"
        serializer.save(emp_des=emp_des)


emp_create = EmpCreate.as_view()


class DepCreate(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepSerializer


dep_create = DepCreate.as_view()