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

from .models import Tecnologia, Competencia, Formacao

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'