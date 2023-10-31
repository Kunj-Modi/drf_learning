import json

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET'])
def hey(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        print("error")
    data['params'] = request.GET
    return Response(data)


class GetUsers(APIView):
    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
