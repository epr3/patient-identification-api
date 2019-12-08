from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from custom_authentication.authentication import JWTAuthentication


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)