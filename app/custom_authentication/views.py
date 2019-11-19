from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from .models import User, RefreshToken


@api_view(['POST'])
def login(request):
    user = authenticate(request, **request.data)
    if user is not None:
        payload = {
            'context': {
                'id': user.id.__str__(),
                'is_medic': user.is_medic,
                'is_staff': user.is_staff,
                'is_medic': user.is_medic,
                'is_superuser': user.is_superuser
            },
            'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_ACCESS_EXP_DELTA_SECONDS)
        }

        access_token = jwt.encode(
            payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        refresh_token = jwt.encode(
            payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
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
