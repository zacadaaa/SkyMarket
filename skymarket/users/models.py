from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    choices = ((USER, USER), (ADMIN, ADMIN))


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    email = models.EmailField(unique=True, max_length=100)
    role = models.CharField(max_length=5,
                            choices=UserRoles.choices,
                            default=UserRoles.USER,
                            verbose_name="Роль пользователя",
                            help_text="Выберите роль пользователя", )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = PhoneNumberField(verbose_name="Телефон для связи")
    is_active = models.BooleanField(verbose_name="Аккаунт активен")
    image = models.ImageField(
        upload_to='images',
        verbose_name="фото",
        blank=True,
    )

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
