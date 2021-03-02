from admin_panel.models import Tour
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (AdminHomePageView, CreateTourView, TourDetailView, TourDeleteView, TourUpdateView, ajax_delete_images)

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
    path("home/", AdminHomePageView.as_view(), name="admin_home_view"),
    path("tour/create/", CreateTourView.as_view(), name="create_tour_view"),
    path("tour/<int:pk>", TourDetailView.as_view(), name="tour_detail_view"),
    path("tour/<int:pk>/delete", TourDeleteView.as_view(), name="tour_delete_view"),
    path("tour/<int:pk>/update", TourUpdateView.as_view(), name="tour_update_view"),
    
    path("ajax/delete-images", ajax_delete_images, name="ajax_delete_images")
]