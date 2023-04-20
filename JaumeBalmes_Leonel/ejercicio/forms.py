from django.forms import ModelForm
from .models import Student, Teacher
from django.forms import ModelForm
from .models import MiTabla, Student, Teacher

class MiTablaForm(ModelForm):
    class Meta:
        model = MiTabla
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
