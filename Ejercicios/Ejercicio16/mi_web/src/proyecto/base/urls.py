from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, ActualizarTarea, EliminarTarea, EliminarTarea

urlpatterns = [
    path('', ListaPendientes.as_view(), name='pendientes'),
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
    path('actualizar-tarea/<int:pk>/', ActualizarTarea.as_view(), name='actualizar_tarea'),
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
]