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
        access_payload = {
            'context': {
                'id': user.id.__str__(),
                'is_medic': user.is_medic,
                'is_staff': user.is_staff,
                'is_medic': user.is_medic,
                'is_superuser': user.is_superuser
            },
            'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_ACCESS_EXP_DELTA_SECONDS)
        }

        refresh_payload = {
            'context': {
                'id': user.id.__str__(),
                'is_medic': user.is_medic,
                'is_staff': user.is_staff,
                'is_medic': user.is_medic,
                'is_superuser': user.is_superuser
            },
            'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_REFRESH_EXP_DELTA_SECONDS)
        }

        access_token = jwt.encode(
            access_payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        refresh_token = jwt.encode(
            refresh_payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        response = Response({'access_token': access_token},
                            status=status.HTTP_200_OK)
        response.set_cookie(key='refresh_token', value=refresh_token, expires=datetime.utcnow(
        ) + timedelta(seconds=settings.JWT_REFRESH_EXP_DELTA_SECONDS), httponly=True)
        return response
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
