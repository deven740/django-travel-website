from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"
    context_object_name = "hello"

    # Pass extra data to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(context)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # Pass single variables
        context["temporary"] = "Hello World"
        context["hola"] = "World Hello"

        # Pass dictionary
        context["dict"] = [
            {"me": "My gee", "be": "My bee"},
            {"me": "Baby", "be": "Boba"},
        ]
        return context
