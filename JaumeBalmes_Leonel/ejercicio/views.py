from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



def students(request):
    students = [
        {"id": 1, "nombre": "Leonel", "apellidos": "García Martínez", "edad": 23},
        {"id": 2, "nombre": "Raul", "apellidos": "Pérez López", "edad": 22},
        {"id": 3, "nombre": "Aitor", "apellidos": "González Sánchez", "edad": 24},
        {"id": 4, "nombre": "Roger", "apellidos": "Martín Torres", "edad": 21},
        {"id": 5, "nombre": "Pere", "apellidos": "Navarro García", "edad": 25},
        {"id": 6, "nombre": "Faro", "apellidos": "Díaz Pérez", "edad": 20},
    ]
    context = {'students': students}
    return render(request, 'students.html', context)

def teachers(request):
    teachers = [
        {"id": 1, "nombre": "Roger", "apellidos": "Fernández Gómez", "edad": 35},
        {"id": 2, "nombre": "Pere", "apellidos": "Ramírez Jiménez", "edad": 42},
        {"id": 3, "nombre": "Faro", "apellidos": "Ortiz Castro", "edad": 38},
    ]
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)

