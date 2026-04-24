from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

from .models import Licenciatura

class LicenciaturaForm(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = '__all__'