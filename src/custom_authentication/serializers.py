from django.db.models import UUIDField
from rest_framework import serializers
from .models import RefreshToken, User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User

class RefreshTokenSerializer(serializers.ModelSerializer):
  class Meta:
    model = RefreshToken
    fields = ['token', 'expiry_date', 'user']
