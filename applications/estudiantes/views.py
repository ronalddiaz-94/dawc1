from errno import ESTALE
from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView)
from .models import Estudiante

class StudentsView(ListView):
    template_name = "students.html"
    model = Estudiante
    context_object_name= "estudiantes"
    ordering= "matStudent"

class StudentCreateView(CreateView):
    template_name = "addStudent.html"
    model = Estudiante
    fields = ("__all__")
    success_url = "/students"

class StudenteUpdateView(UpdateView):
    template_name = "updtStudent.html"
    model = Estudiante
    fields = ("__all__")
    success_url = "/students"

class StudentDeleteView(DeleteView):
    template_name = "delStudent.html"
    model = Estudiante
    success_url = "/students"
    context_object_name = "estudiante"


