from django.http import Http404
from django.shortcuts import render, redirect
from .forms import MiTablaForm

student_list = [
    {"id": 1, "nombre": "Leonel", "apellidos": "García Martínez", "edad": 23},
    {"id": 2, "nombre": "Raul", "apellidos": "Pérez López", "edad": 22},
    {"id": 3, "nombre": "Aitor", "apellidos": "González Sánchez", "edad": 24},
    {"id": 4, "nombre": "Roger", "apellidos": "Martín Torres", "edad": 21},
    {"id": 5, "nombre": "Pere", "apellidos": "Navarro García", "edad": 25},
    {"id": 6, "nombre": "Faro", "apellidos": "Díaz Pérez", "edad": 20},
]

teacher_list = [
    {"id": 1, "nombre": "Roger", "apellidos": "Fernández Gómez", "edad": 35},
    {"id": 2, "nombre": "Pere", "apellidos": "Ramírez Jiménez", "edad": 42},
    {"id": 3, "nombre": "Faro", "apellidos": "Ortiz Castro", "edad": 38},
]

def index(request):
    return render(request, 'index.html')

def students(request):
    context = {'students': student_list}
    return render(request, 'students.html', context)

def teachers(request):
    context = {'teachers': teacher_list}
    return render(request, 'teachers.html', context)

def student_detail(request, student_id):
    student = next((s for s in student_list if s['id'] == student_id), None)
    if student is None:
        raise Http404("Student not found")
    return render(request, 'student_detail.html', {'student': student})

def teacher_detail(request, teacher_id):
    teacher = next((t for t in teacher_list if t['id'] == teacher_id), None)
    if teacher is None:
        raise Http404("Teacher not found")
    return render(request, 'teacher_detail.html', {'teacher': teacher})




def formulario(request):
    form = MiTablaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid(): form.save(); return redirect('ejercicio:index')
    return render(request, 'formulario.html', {'form': form})




