from django.shortcuts import render, HttpResponse
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
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
    
    def get(self, request, *args, **kwargs):
        print('hello')
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        query = self.request.GET.get('query', None)
        queryset = Tour.objects.all()
        
        if query:
            queryset = queryset.filter(name__icontains=query)
        
        return queryset


class CreateTourView(CreateView):
    model = Tour
    template_name = "admin_panel/create_tour.html"
    fields = "__all__"

    def form_valid(self, form):
        tour = form.save()
        number_of_images = len(self.request.FILES.getlist("extra_images"))
        if number_of_images > 0:
            for image in self.request.FILES.getlist("extra_images"):
                TourImage.objects.create(tour=tour, image=image)
        return super().form_valid(form)


class TourDetailView(DetailView):
    model = Tour
    template_name = "admin_panel/tour_detail.html"


class TourDeleteView(DeleteView):
    model = Tour
    success_url = reverse_lazy("admin_home_view")


class TourUpdateView(UpdateView):
    model = Tour
    template_name = "admin_panel/update_tour.html"
    fields = "__all__"

    def form_valid(self, form):
        tour = form.save()
        number_of_images = len(self.request.FILES.getlist("extra_images"))
        if number_of_images > 0:
            for image in self.request.FILES.getlist("extra_images"):
                TourImage.objects.create(tour=tour, image=image)
        return super().form_valid(form)


def ajax_delete_images(request):

    image_list = request.POST.getlist("image_list[]")

    for image_id in image_list:
        TourImage.objects.get(id=int(image_id)).delete()

    return JsonResponse({"success": "Images Deleted Successfully"})
