# -*- coding: UTF-8 -*-
from django.urls import path
from trade.views import HomeView, ProductDetailView, ProductEditView, ProductDeleteView, \
    ProductCreateView, CategoryView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug>', ProductDetailView.as_view(), name='product_detail'),
    path('<slug>/edit', ProductEditView.as_view(), name='product_edit'),
    path('<slug>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('new/', ProductCreateView.as_view(), name='product_add'),
    path('category/<slug>', CategoryView.as_view(), name='category_detail'),
]
