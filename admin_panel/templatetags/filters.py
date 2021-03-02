from django import template

register = template.Library()

@register.filter(name='tour_image_url')
def tour_image_url(tour):
    url = tour.tourimage.all()[0].image.url
    return url