from itertools import count
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import ImageField
from django.contrib.auth import get_user_model
 
User = get_user_model()

"""class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_activate = models.BooleanField(default=False)
    is_role = models."""


class Chapter(models.Model):
    name = models.CharField(max_length=50)


class Announcement_User(models.Model):
    image = models.ImageField(verbose_name="Фото")
    chapter = models.ForeignKey(Chapter, on_delete=models.PROTECT)
    country = models.CharField()


class Location_User(models.Model):
    announcement = models.ForeignKey(Announcement_User, on_delete=CASCADE)
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта