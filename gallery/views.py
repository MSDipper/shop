from django.shortcuts import render
from gallery.models import MyLife, ImageStyleLife
from django.views.generic.base import TemplateView


class Gallery():
    def get_life(self):
        return MyLife.objects.all()

    def get_image(self):
        return ImageStyleLife.objects.all()


class GalleryView(Gallery, TemplateView):
    template_name = 'gallery/gallery.html'