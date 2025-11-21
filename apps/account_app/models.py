from django.contrib.auth.base_user import BaseUserManager as BUM, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_jalali.db import models as jmodels

# region CustomUserManagerModel
class UserManager(BUM):
    def create_user(self, first_name, last_name, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('A phone number must be provided')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            **extra_fields
        )
# endregion

# region UserModel
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='First-Name', max_length=255)
    last_name = models.CharField(verbose_name='Last-Name', max_length=255)
    phone = models.CharField(verbose_name='Phone', max_length=11, unique=True)
    is_active = models.BooleanField(verbose_name='Is-Active', default=False)
    is_staff = models.BooleanField(verbose_name='Is-Staff', default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name}: {self.phone}'

    @property
    def latest_otp(self):
        return self.otps.filter(is_verified=False).last()
# endregion

# region OtpModel
class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    code = models.CharField(max_length=6)
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.phone} - {self.code}"
# endregion