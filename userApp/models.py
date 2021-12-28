from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields["is_active"] = True
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name="email address", unique=True,)
    username = models.CharField(_("username"), max_length=150,)
    is_active = models.BooleanField(default=True)
    is_loan_provider = models.BooleanField(default=False)
    is_loan_customer = models.BooleanField(default=False)
    is_bank_personnel = models.BooleanField(default=False)


    # verification_code = models.CharField(
    #     max_length=10, default=rand_int_4digits, null=True, blank=True
    # )

    # password_reset_code = models.CharField(max_length=10, null=True, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
