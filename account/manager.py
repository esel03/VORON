from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
#from .models import CustomUser

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user
'''
    def update(self, id_user, **extra_fields):
        if extra_fields.get('password'):
            password = CustomUser.set_password(extra_fields.get('password'))
            return CustomUser.objects.filter(pk=id_user).update(password, **extra_fields)
        else:
            return CustomUser.objects.filter(pk=id_user).update(**extra_fields)
'''
















