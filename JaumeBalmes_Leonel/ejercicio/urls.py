from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.students, name='students'),
    path('teachers', views.teachers, name='teachers'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
]


