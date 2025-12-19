from django.urls import path,include 
from .views import ProfileAPI,login_page
urlpatterns=[
    path("login/", login_page,name="login"),
    path("profile/", ProfileAPI.as_view(),name="profile")
    ]