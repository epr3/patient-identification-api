from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import ObjectDoesNotExist


class PatientAPIBackend(ModelBackend):
    def authenticate(self, request, pnc=None, password=None, **kwargs):
        try:
            user = User.objects.get(pnc=pnc)
            if user.check_password(password):
                return user
        except ObjectDoesNotExist:
            return None
