from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    CINTURONES = [
        ("Blanco", "Blanco"),
        ("Amarillo", "Amarillo"),
        ("Naranja", "Naranja"),
        ("Verde", "Verde"),
        ("Azul", "Azul"),
        ("Marrón", "Marrón"),
        ("Negro", "Negro"),
    ]
    cinturon = models.CharField(max_length=20, choices=CINTURONES, default="Blanco")

    fecha_ingreso = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("Activo", "Activo"),
            ("Inactivo", "Inactivo"),
            ("Retirado", "Retirado"),
        ],
        default="Activo"
    )

    def __str__(self):
        return f"{self.nombre} - {self.cinturon}"

    class Meta:
        db_table = "alumnos"  # aquí definimos el nombre exacto de la tabla
