from django.db import models
from django.contrib.auth.models import AbstractUser
# from trade.models import Product
import os


def avatar_upload_to(instance, filename):
    return os.path.join('media/avatars', instance.user.username + os.path.splitext(filename)[1])


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', verbose_name='аватарка', blank=True)
    money = models.DecimalField(default=100, decimal_places=2, max_digits=20, verbose_name='счет')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # def get_product_list(self):
    #     user = self.username
    #     qs = Product.objects.filter(owner__username=user)
