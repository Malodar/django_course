from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from trade.models import Product, Category, Cart, CartItem
from accounts.models import CustomUser
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError
from django.shortcuts import get_object_or_404
from django.contrib import messages


class HomeView(ListView):
    model = Product
    template_name = 'trade/home.html'
    paginate_by = 30
    ordering = 'name'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'trade/product_detail.html'


class ProductEditView(UpdateView):
    model = Product
    template_name = 'trade/product_edit.html'
    fields = ('price', 'name', 'description', 'image',)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'trade/product_delete.html'
    success_url = reverse_lazy('home')


class ProductCreateView(CreateView):
    def get_slug_field(self):
        return slugify(translit(self.request.POST['name'], reversed=True), allow_unicode=True)
    model = Product
    template_name = 'trade/product_add.html'
    fields = ('name', 'image', 'price', 'description', 'category')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        try:
            form.instance.slug = slugify(translit(self.request.POST['name'], reversed=True), allow_unicode=True)
        except LanguageDetectionError:
            form.instance.slug = slugify(self.request.POST['name'], allow_unicode=True)
        return super().form_valid(form)


class CategoryView(ListView):
    template_name = 'trade/category_detail.html'
    category = None

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


def cart_view(request):
    return render(request, 'trade/cart.html')


def add_to_cart(request, slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=slug)
    cart.add_to_cart(product.slug)
    return HttpResponseRedirect(reverse('cart_view'))


def remove_from_cart(request, slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=slug)
    cart.remove_from_cart(product.slug)
    return HttpResponseRedirect(reverse('cart_view'))


def make_order(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    buyer_id = request.session['_auth_user_id']
    buyer = CustomUser.objects.get(id=buyer_id)
    cart_total = cart.calculate_total()
    if cart_total < buyer.money:
        for cart_item in cart.items.all():
            seller_id = cart_item.product.owner_id
            seller = CustomUser.objects.get(id=seller_id)

            seller.money += cart_item.product.price
            buyer.money -= cart_item.product.price
            cart_item.product.owner_id = buyer_id

            seller.save()
            cart_item.product.save()
            cart.remove_from_cart(cart_item.product.slug)
        buyer.save()
        return render(request, 'trade/success_trade.html')
    else:
        messages.warning(request, 'Сумма заказа больше, чем у вас денег. Удалите лишние товары.')
        return HttpResponseRedirect(reverse('cart_view'))
