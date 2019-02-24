# -*- coding: UTF-8 -*-
from django.urls import path
from trade.views import HomeView, ProductDetailView, ProductEditView, ProductDeleteView, \
    ProductCreateView, CategoryView, cart_view, add_to_cart, remove_from_cart, make_order


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug>', ProductDetailView.as_view(), name='product_detail'),
    path('<slug>/edit', ProductEditView.as_view(), name='product_edit'),
    path('<slug>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('new/', ProductCreateView.as_view(), name='product_add'),
    path('category/<slug>', CategoryView.as_view(), name='category_detail'),
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart_view'),
    path('remove/<slug>', remove_from_cart, name='remove_from_cart'),
    path('cart/trade', make_order, name='make_order'),
]
