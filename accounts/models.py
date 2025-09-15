from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, full_name, mobile, email, password=None):
        if not email:
            raise ValueError("You did not give your email address")
        if not full_name:
            raise ValueError("You did not give your name")
        
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            mobile=mobile,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, mobile, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            full_name=full_name,
            mobile=mobile,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    SELLER = 1
    CUSTOMER = 2
    ROLE_CHOICE = (
        (SELLER, "Seller"),
        (CUSTOMER, "Customer"),
    )

    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'mobile']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
