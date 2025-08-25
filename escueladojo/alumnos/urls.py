from django.urls import path
from . import views  # Importamos las vistas de la aplicación alumnos

app_name = 'alumnos'

urlpatterns = [
    path('', views.lista_alumnos, name='lista'),
    path('nuevo/', views.create_alumno, name='nuevo'),
    path('editar/<int:pk>/', views.edit_alumno, name='editar'),
    path('eliminar/<int:pk>/', views.delete_alumno, name='eliminar'),
]