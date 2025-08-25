from django.contrib import admin
from django.urls import path, include
from alumnos.views import inicio  # Importa la vista inicio desde la app alumnos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  # Página de inicio de la escuela de karate
    path('alumnos/', include(('alumnos.urls', 'alumnos'), namespace='alumnos')),  # Rutas para las vistas de alumnos
]
