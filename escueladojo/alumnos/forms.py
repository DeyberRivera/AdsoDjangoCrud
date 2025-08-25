from django import forms #importamos el modulo forms de Django
from .models import Alumno #Importamos el modelo alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'nombre',
            'edad',
            'telefono',
            'email',
            'cinturon',
            'estado'
        ]