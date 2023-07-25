"""
Classe reponsável por todos os models da API.
"""
from __future__ import annotations
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(
            self, email: str, password: str, **kwargs) -> User:
        username = kwargs.pop('username')

        if not username or not password or not email:
            raise ValueError(
                'ValueError: username, password and email cannot be null.')

        user: User = self.model(
            email=self.normalize_email(email),
            password=password,
            username=username,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
            self, username: str,  password: str, **kwargs) -> User:

        user: User = self.create_user(
            username, password, kwargs
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=40, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    @property
    def is_staff(self) -> bool:
        return self.is_admin
