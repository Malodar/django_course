# -*- coding: UTF-8 -*-
from trade.models import Category, Cart, Product
from accounts.models import CustomUser


def get_categories(request):
    qs_categories = Category.objects.all().order_by('category_name')
    extra_context = {'category_list': qs_categories,
                     }
    return extra_context


def get_cart(request):
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
    cart_total = cart.calculate_total()
    extra_context = {
                     'cart': cart,
                     'cart_total': cart_total,
                     }
    return extra_context


def get_filtered_prods(request):
    try:
        user_id = request.session['_auth_user_id']
        prods = Product.objects.filter(owner_id=user_id)
        extra_context = {
            'prods': prods,
        }
    except:
        extra_context = {
            'prods': '',
        }
    return extra_context
