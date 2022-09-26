from django.forms import ModelForm
from .models import Chamado

class ChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        fields = ['title','description','categoria','status']