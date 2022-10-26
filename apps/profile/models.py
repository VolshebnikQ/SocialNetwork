import os

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model"""
    SEX = [
        ('none', ' --- '),
        ('male', 'Мужской'),
        ('female', 'Женский')
    ]

    def imagepath(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'avatar.{ext}'
        path = f'users/{instance.username}/{filename}'
        if os.path.exists(path):
            os.remove(path)
        return path

    about = models.TextField(blank=True, null=True, verbose_name='Обо мне')
    city = models.CharField(
        blank=True,
        max_length=100,
        null=True,
        verbose_name='Город')
    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name='День рождения')
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name='Номер телефона')
    avatar = models.ImageField(
        default='default_avatar.png',
        upload_to=imagepath)
    sex = models.CharField(blank=True, choices=SEX, max_length=6, null=True)

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'User: {self.username}'


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    users_friend = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users_friend')
    confirmed = models.BooleanField('Подтверждено', default=False)

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return f'{self.user} -> {users_friend}'
