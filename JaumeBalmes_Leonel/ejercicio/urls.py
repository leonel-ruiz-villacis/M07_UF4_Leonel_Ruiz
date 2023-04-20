from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('teachers', views.teachers, name='teachers'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('formulario/', views.formulario, name='formulario'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('update_teacher/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
]


