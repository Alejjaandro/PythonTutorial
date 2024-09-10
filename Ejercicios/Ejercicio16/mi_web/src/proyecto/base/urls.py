from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, ActualizarTarea, EliminarTarea, EliminarTarea, InicioSesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ListaPendientes.as_view(), name='pendientes'),
    path('iniciar-sesion/', InicioSesion.as_view(), name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(next_page='iniciar_sesion'), name='cerrar_sesion'),
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
    path('actualizar-tarea/<int:pk>/', ActualizarTarea.as_view(), name='actualizar_tarea'),
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
]