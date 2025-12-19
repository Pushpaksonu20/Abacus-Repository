from django.urls import path
from .views import LoginAPI, ProfileAPI

urlpatterns = [
    path("login/", LoginAPI.as_view(), name="token-login"),
    path("profile/", ProfileAPI.as_view(), name="profile"),
]
