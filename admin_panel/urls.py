from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (AdminHomePageView, )

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="admin_panel/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    
    path("home/", AdminHomePageView.as_view(), name="admin_home_view")
]