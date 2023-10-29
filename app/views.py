import json

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hey(request, *args, **kwargs):
    print(args, kwargs)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        print("error")
    data['params'] = request.GET
    return Response(data)
