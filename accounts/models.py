from django.db import models
from django.contrib.auth.models import AbstractUser
import os


def avatar_upload_to(instance, filename):
    return os.path.join('media/avatars', instance.user.username + os.path.splitext(filename)[1])


class CustomUser(AbstractUser):
    # avatar = models.ImageField(upload_to='avatars', verbose_name='аватарка',
    #                            default='static/img/default_avatar.jpg')
    avatar = models.ImageField(upload_to='avatars', verbose_name='аватарка', blank=True)
    money = models.DecimalField(default=100, decimal_places=2, max_digits=20, verbose_name='счет')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

