from django.db.models import UUIDField
from rest_framework import serializers
from .models import RefreshToken, User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User

class RefreshTokenSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(
  ), pk_field=serializers.UUIDField(format='hex_verbose'))
  class Meta:
    model = RefreshToken
    fields = ['token', 'expiry_date', 'user']
