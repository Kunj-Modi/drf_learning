from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def student(request, *args, **kwargs):
    instance = Student.objects.all().order_by('?').first()
    data = StudentSerializer(instance).data
    return Response(data)


@api_view(['POST'])
def add_student(request, *args, **kwargs):
    data = request.data
    print(data)
    serializer = StudentSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({'error': 'invalid data'})
