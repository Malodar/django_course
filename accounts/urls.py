# -*- coding: UTF-8 -*-
from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, UserProfileView, UserProfileEditView


urlpatterns = [
    path('new_user/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('<int:pk>', UserProfileView.as_view(), name='user_profile'),
    path('<int:pk>/edit', UserProfileEditView.as_view(), name='user_edit'),
]
