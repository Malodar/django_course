from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# from django.template.defaultfilters import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец')
    name = models.CharField(max_length=200, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, auto_created=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', verbose_name='Категория')
    image = models.ImageField(upload_to='product_images', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        index_together = (('id', 'slug'),)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #         super(Product, self).save()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


# class Cart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
