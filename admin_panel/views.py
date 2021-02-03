from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.views import View


class AdminHomePageView(TemplateView):
    template_name = "admin_panel/admin_home.html"

