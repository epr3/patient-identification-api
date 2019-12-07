from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from .serializers import RefreshTokenSerializer


class Login(APIView):
    def post(self, request):
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
            serializer = RefreshTokenSerializer(
                data={'token': refresh_token.decode('utf-8'), 'user': user.id, 'expiry_date': (datetime.utcnow() + timedelta(seconds=settings.JWT_REFRESH_EXP_DELTA_SECONDS)).strftime('%Y-%m-%d')})
            if serializer.is_valid():
                serializer.save()
                response = Response({'access_token': access_token},
                                    status=status.HTTP_200_OK)
                response.set_cookie(key='refresh_token', value=refresh_token, expires=datetime.utcnow(
                ) + timedelta(seconds=settings.JWT_REFRESH_EXP_DELTA_SECONDS), httponly=True)
                return response
            else:
                print(serializer.errors)
                return Response('Error while logging in', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('Invalid PNC or password', status=status.HTTP_401_UNAUTHORIZED)
