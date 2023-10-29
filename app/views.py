from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hey(request):
    data = {'name': 'kunj', 'code': 7183}
    return Response(data)
