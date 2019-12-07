import jwt
from django.contrib.auth.models import User
from rest_framework import HTTP_HEADER_ENCODING, authentication


class JWTAuthentication(authentication.BaseAuthentication):
    def get_header(self, request):
        header = request.META.get('Authorization')
        if isinstance(header, str):
            header = header.encode(HTTP_HEADER_ENCODING)
        return header

    def get_user(self, validated_token):
        user = User.objects.get(pk=validated_token.context.id)

    def authenticate(self, request):
        header = get_header(request)
        decoded_token = jwt.decode(header)
        return super().authenticate(request)
