from uuid import uuid4
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from polymorphic.models import PolymorphicModel


class User(AbstractBaseUser, PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    pnc = models.CharField(max_length=13, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'pnc'
    REQUIRED_FIELDS = []


class Medic(User):
    pass


class Patient(User):
    insure_code = models.CharField(max_length=20)
    expiry_date = models.DateField()
    assigned_medic = models.ForeignKey(Medic, on_delete=models.DO_NOTHING)
