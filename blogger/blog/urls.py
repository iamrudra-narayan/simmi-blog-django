from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="Home"),
    path("register/", views.register, name="Register"),
    path("login/", views.login, name="Login"),
    path("account/", views.account, name="account"),
    path('logout/', views.logout_user, name="Logout")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)