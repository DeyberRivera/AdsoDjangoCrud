from alumnos.models import Alumno
from datetime import date, timedelta
import random

nombres = [
    "Ana Torres", "Luis Martínez", "Carlos Gómez", "María Rodríguez", "Juan Pérez",
    "Lucía Ramírez", "Pedro Sánchez", "Camila Herrera", "Esteban Ruiz", "Diana Castro",
    "José Vargas", "Laura Mendoza", "Tomás Rivera", "Paula Suárez", "Andrés León",
    "Valentina Ortiz", "Gabriel Morales", "Mónica Silva", "Raúl Jiménez", "Isabela López",
    "David Castro", "Natalia Peña", "Jorge Díaz", "Daniela Ríos", "Santiago Paredes",
    "Fernanda Acosta", "Sebastián Villa", "Carolina Reyes", "Ricardo Bravo", "Luciana Vega",
    "Matías Soto", "Alejandra Paz", "Felipe Duarte", "Manuela Cruz", "Diego Cárdenas",
    "Ángela Mejía", "Brayan Torres", "Sara Lozano", "Iván Guerrero", "Juliana Navarro",
    "Emilio Pino", "Nicole Fajardo", "Cristian Bernal", "Renata Quiroz", "Franco Orozco",
    "Melissa Tapia", "Alan Robles", "Martina Espinosa", "Samuel Vivas", "Rosa Rivera"
]

cinturones = ['Blanco', 'Amarillo', 'Naranja', 'Verde', 'Azul', 'Marrón', 'Negro']
estados = ['Activo', 'Inactivo']

alumnos = []

for nombre in nombres:
    edad = random.randint(13, 21)
    telefono = f"300{random.randint(1000000, 9999999)}"
    email = nombre.lower().replace(" ", ".") + "@example.com"
    cinturon = random.choice(cinturones)
    fecha_ingreso = date.today() - timedelta(days=random.randint(30, 1000))
    estado = random.choice(estados)

    alumnos.append(Alumno(
        nombre=nombre,
        edad=edad,
        telefono=telefono,
        email=email,
        cinturon=cinturon,
        fecha_ingreso=fecha_ingreso,
        estado=estado
    ))

Alumno.objects.bulk_create(alumnos)
print(f"{len(alumnos)} estudiantes creados exitosamente.")