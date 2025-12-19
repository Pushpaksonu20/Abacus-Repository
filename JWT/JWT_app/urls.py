from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("jwt/login/", TokenObtainPairView.as_view(), name="jwt_login"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
]
