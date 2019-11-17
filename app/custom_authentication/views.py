from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
  user = authenticate(request, **request.data)
  if user is not None:
    return Response('Login', status=status.HTTP_200_OK)
  else:
    return Response('Invalid PNC or password', status=status.HTTP_401_UNAUTHORIZED)

# TODO
@api_view(['POST'])
def register(request):
  user = authenticate(request.data)
  if user is not None:
    return Response('Login', status=status.HTTP_200_OK)
  else:
    return Response('Invalid PNC or password', status=status.HTTP_401_UNAUTHORIZED)
