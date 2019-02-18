from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Product, Category
from django.urls import reverse_lazy
# from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.utils.translation.trans_real import to_language


class HomeView(ListView):
    model = Product
    template_name = 'trade/home.html'


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
        return slugify(self.request.POST['name'], allow_unicode=True)
    model = Product
    template_name = 'trade/product_add.html'
    fields = ('name', 'image', 'price', 'description', 'category')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(self.request.POST['name'], allow_unicode=True)
        return super().form_valid(form)
