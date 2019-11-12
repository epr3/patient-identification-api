from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
  email = models.EmailField(unique=True)
  first_name = models.CharField()
  last_name = models.CharField()
  date_of_birth = models.DateField()
  pnc = models.CharField(max_length=13)
  insure_code = models.CharField()
  expiry_date = models.DateField()


  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
