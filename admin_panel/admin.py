from django.contrib import admin

from .models import Tour, TourImage

class TourImageAdmin(admin.StackedInline):
    model = TourImage

@admin.register(Tour)    
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageAdmin]
    
    class Meta:
        model = Tour

# admin.site.Re
