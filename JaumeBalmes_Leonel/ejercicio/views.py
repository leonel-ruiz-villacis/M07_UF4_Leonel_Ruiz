from django.shortcuts import render, redirect, get_object_or_404

from .forms import MiTablaForm, StudentForm, TeacherForm
from .models import Student, Teacher

def index(request):
    return render(request, 'index.html')

def students(request):
    student_list = Student.objects.all()
    return render(request, 'students.html', {'students': student_list})

def teachers(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teacher_list})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def formulario(request):
    form = MiTablaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ejercicio:index')
    return render(request, 'formulario.html', {'form': form})

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'student_form.html', {'form': form})

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'student_form.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('students')

def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teachers')
    return render(request, 'teacher_form.html', {'form': form})

def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teachers')
    return render(request, 'teacher_form.html', {'form': form})

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('teachers')



