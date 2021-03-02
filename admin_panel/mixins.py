from .models import Tour, TourImage

class TourImageMixin:
    model = Tour
    fields = "__all__"

    def form_valid(self, form):
        tour = form.save()
        for image in self.request.FILES.getlist('extra_images'):
            TourImage.objects.create(tour=tour, image=image)
        return super().form_valid(form)