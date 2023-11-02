from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import Department, Employee
from .serializers import DepSerializer, EmpSerializer


class EmpRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer


emp_retrieve = EmpRetrieve.as_view()


class DepRetrieve(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepSerializer


dep_retrieve = DepRetrieve.as_view()
