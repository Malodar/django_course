from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Product, Category
from django.urls import reverse_lazy
from django.utils.text import slugify
from transliterate import translit
from django.shortcuts import get_object_or_404


class HomeView(ListView):
    model = Product
    template_name = 'trade/home.html'
    paginate_by = 30
    qs = Category.objects.all()
    extra_context = {'category_list': qs}


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
        form.instance.slug = slugify(translit(self.request.POST['name'], reversed=True), allow_unicode=True)
        return super().form_valid(form)


class CategoryView(ListView):
    template_name = 'trade/category_detail.html'
    category = None

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = self.category
        return context
