from django.shortcuts import render, HttpResponse
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from .mixins import TourImageMixin
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Tour, TourImage
from django.http import JsonResponse


class AdminHomePageView(ListView):
    model = Tour
    context_object_name = "tours"
    paginate_by = 4
    template_name = "admin_panel/view_tours.html"
    
    def get_queryset(self):
        query = self.request.GET.get('query', None)
        queryset = Tour.objects.all()
        
        if query:
            queryset = queryset.filter(name__icontains=query)
        
        return queryset


class CreateTourView(TourImageMixin, CreateView):
    template_name = "admin_panel/create_tour.html"
    

class TourUpdateView(TourImageMixin, UpdateView):
    template_name = "admin_panel/update_tour.html"
    


class TourDetailView(DetailView):
    model = Tour
    template_name = "admin_panel/tour_detail.html"


class TourDeleteView(DeleteView):
    model = Tour
    success_url = reverse_lazy("admin_home_view")


def ajax_delete_images(request):

    image_list = request.POST.getlist("image_list[]")

    for image_id in image_list:
        TourImage.objects.get(id=int(image_id)).delete()

    return JsonResponse({"success": "Images Deleted Successfully"})
