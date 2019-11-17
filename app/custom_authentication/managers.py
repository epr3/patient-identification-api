from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, pnc, password, **extra_fields):
        """
        Creates and saves a User with the given pnc and password.
        """
        if not pnc:
            raise ValueError('The given pnc must be set')
        user = self.model(pnc=pnc, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, pnc, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(pnc, password, **extra_fields)

    def create_superuser(self, pnc, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('last_name', 'superuser')
        extra_fields.setdefault('first_name', 'superuser')
        extra_fields.setdefault('date_of_birth', '1990-01-01')
        extra_fields.setdefault('email', 'test@test.com')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(pnc, password, **extra_fields)
