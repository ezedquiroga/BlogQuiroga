from django.contrib import admin
from django.urls import path, include
from Account.views import login_account, register_account
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_account, name="AccountLogin"),
    path('registrar/', register_account, name="AccountRegistrar"),
    path('logout/', LogoutView.as_view(template_name="Account/logout.html"), name="AccountLogout"),
]