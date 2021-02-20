from django.db import models
from django.urls import reverse


class Tour(models.Model):
    
    tour_types = (
        
        ("family", "Family"),
        ("solo", "Solo"),
        ("friends", "Friends"),
        ("adventure", "Adventure"),
        ("nature", "Nature"),
        ("religious", "Religious"),
        ("wildlife", "WildLife"),
    )
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=25, choices=tour_types)
    date = models.DateField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tour_detail_view', args=[str(self.id)])
    
class TourImage(models.Model):
    tour = models.ForeignKey(Tour, default=None, on_delete=models.CASCADE, related_name='tourimage')
    image = models.FileField(upload_to='images/')
    
    def __str__(self):
        return self.tour.name
        
