# -*- coding: UTF-8 -*-
from trade.models import Category, Cart


def get_categories(request):
    qs_categories = Category.objects.all().order_by('category_name')
    # qs_cart = Cart.objects.first()
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
    extra_context = {'category_list': qs_categories,
                     'cart': cart,
                     }
    return extra_context
