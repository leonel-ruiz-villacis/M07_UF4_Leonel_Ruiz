from django.forms import ModelForm
from .models import MiTabla


class MiTablaForm(ModelForm):
    class Meta:
        model = MiTabla
        fields = '__all__'  
