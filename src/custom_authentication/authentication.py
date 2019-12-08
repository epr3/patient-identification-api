from jwt import exceptions, decode
from django.conf import settings
from rest_framework import HTTP_HEADER_ENCODING, authentication, exceptions as rest_exceptions
from .models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def get_header(self, request):
        header = request.META.get('HTTP_AUTHORIZATION')
        if isinstance(header, str):
            header = header.encode(HTTP_HEADER_ENCODING)
        return header

    def get_user(self, validated_token):
        try:
            user = User.objects.get(
                pk=validated_token.get('context').get('id'))
            return user
        except User.DoesNotExist:
            raise rest_exceptions.AuthenticationFailed('No such user')

    def authenticate(self, request):
        header = self.get_header(request)
        if header is not None:
            token = header.decode('utf-8').split(' ')[1].encode()
            try:
                decoded_token = decode(token, settings.JWT_SECRET)
            except exceptions.PyJWTError:
                raise rest_exceptions.AuthenticationFailed('Token error')

            return self.get_user(decoded_token), None
        return None
