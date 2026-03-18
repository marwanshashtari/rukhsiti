from django.urls import path
from .views import register_user, current_user_profile

urlpatterns = [
    path("register/", register_user, name="register"),
    path("me/", current_user_profile, name="current_user_profile"),
]