from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import Department, Employee
from .serializers import DepSerializer, EmpSerializer


class EmpCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer


emp_create = EmpCreate.as_view()


class DepCreate(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepSerializer


dep_create = DepCreate.as_view()
