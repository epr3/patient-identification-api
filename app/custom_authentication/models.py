from uuid import uuid4
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    pnc = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_medic = models.BooleanField(default=True)

    USERNAME_FIELD = 'pnc'
    REQUIRED_FIELDS = []

    objects = UserManager()


class RefreshToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    token = models.CharField(max_length=100)
    expiry_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PatientCard(models.Model):
    insure_code = models.CharField(max_length=20)
    expiry_date = models.DateField()
    assigned_medic = models.OneToOneField(User, on_delete=models.DO_NOTHING)
