from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/user_registration.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserLogoutView(LogoutView):
    template_name = 'registration/logout.html'


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'


class UserProfileEditView(UpdateView):
    model = CustomUser
    template_name = 'registration/user_profile_edit.html'
    fields = ['avatar', 'email']
    success_url = reverse_lazy('home')
