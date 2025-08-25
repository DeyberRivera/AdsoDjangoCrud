from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Alumno
from .forms import AlumnoForm

# Listar alumnos con paginación
def lista_alumnos(request):
    alumnos_list = Alumno.objects.all().order_by('-fecha_ingreso')
    paginator = Paginator(alumnos_list, 10)  # 10 por página
    page = request.GET.get('page', 1)

    try:
        alumnos = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        alumnos = paginator.page(1)

    return render(request, 'alumnos/alumno_list.html', {'alumnos': alumnos})


# Crear un alumno
def create_alumno(request):
    form = AlumnoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alumnos:lista')
    return render(request, 'alumnos/alumno_form.html', {'form': form})


# Editar un alumno
def edit_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    form = AlumnoForm(request.POST or None, instance=alumno)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('alumnos:lista')
    return render(request, 'alumnos/alumno_form.html', {'form': form})


# Eliminar un alumno
def delete_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnos:lista')
    return render(request, 'alumnos/alumno_confirm_delete.html', {'alumno': alumno})

def inicio(request):
    context = {
        'escuela': 'DojoKarate',
        'descripcion': 'Escuela de Karate para todas las edades',
    }
    return render(request, 'inicio.html', context)
