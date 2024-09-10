from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Tarea

# Create your views here.
class ListaPendientes(ListView):
    model = Tarea
    template_name = 'pendientes.html'
    context_object_name = 'tareas'


class DetalleTarea(DetailView):
    model = Tarea
    template_name = 'detalle_tarea.html'
    context_object_name = 'tarea'
    
class CrearTarea(CreateView):
    model = Tarea
    template_name = 'crear_tarea.html'
    fields = '__all__'
    success_url = reverse_lazy('pendientes')
    
class ActualizarTarea(UpdateView):
    model = Tarea
    template_name = 'crear_tarea.html'
    fields = '__all__'
    success_url = reverse_lazy('pendientes')

class EliminarTarea(DeleteView):
    model = Tarea
    template_name = 'eliminar_tarea.html'
    context_object_name = 'tarea'
    success_url = reverse_lazy('pendientes')