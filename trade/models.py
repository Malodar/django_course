from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])


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

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product {}".format(self.product.name)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина товаров'
        verbose_name_plural = 'Корзины товаров'

    def add_to_cart(self, slug):
        cart = self
        product = Product.objects.get(slug=slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart(self, slug):
        cart = self
        product = Product.objects.get(slug=slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()
