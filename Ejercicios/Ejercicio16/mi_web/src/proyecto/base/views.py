from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tarea

# Create your views here.
class InicioSesion(LoginView):
    template_name = 'iniciar_sesion.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pendientes')

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'pendientes.html'
    context_object_name = 'tareas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completada=False).count()
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'detalle_tarea.html'
    context_object_name = 'tarea'
    
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    template_name = 'crear_tarea.html'
    fields = ['titulo', 'descripcion', 'completada']
    success_url = reverse_lazy('pendientes')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)
    
class ActualizarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    template_name = 'crear_tarea.html'
    fields = '__all__'
    success_url = reverse_lazy('pendientes')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar_tarea.html'
    context_object_name = 'tarea'
    success_url = reverse_lazy('pendientes')