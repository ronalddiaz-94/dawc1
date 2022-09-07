from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, ListView)
from .models import Carrera

class HomeView(TemplateView):
    template_name = "home.html"

class CarrersView(ListView):
    template_name = "carrers.html"
    model = Carrera
    context_object_name= "carreras"
    ordering= "nameCarrer"

class CarrerViewByInput(ListView):
    template_name= "inputCarrer.html"
    context_object_name=  "cars"

    def get_queryset(self):
        idCarrera = self.request.GET.get("namecar", "")
        listaCarreras = Carrera.objects.filter(nameCarrer=idCarrera)
        return listaCarreras
