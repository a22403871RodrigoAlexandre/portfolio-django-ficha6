from django.shortcuts import render, get_object_or_404
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Formacao
from .forms import ProjetoForm
from .forms import LicenciaturaForm
from .forms import TecnologiaForm, CompetenciaForm, FormacaoForm
from django.shortcuts import redirect


def home_view(request):
    return render(request, 'portfolio/home.html')

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('ucs', 'tfcs').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def docentes_view(request):
    docentes = Docente.objects.prefetch_related('ucs').all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes', 'projetos').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def projetos_view(request):
    projetos = Projeto.objects.select_related('uc').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tfcs_view(request):
    tfcs = TFC.objects.select_related('licenciatura').prefetch_related('orientador', 'tecnologias').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def uc_detail_view(request, uc_id):
    uc = get_object_or_404(UnidadeCurricular, id=uc_id)

    return render(request, 'portfolio/uc_detail.html', {
        'uc': uc
    })

def makingof_view(request):
    return render(request, 'portfolio/makingof.html')

def projeto_create(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()

    return render(request, 'portfolio/projeto_form.html', {'form': form})


def projeto_update(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'portfolio/projeto_form.html', {'form': form})

def projeto_delete(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')

    return render(request, 'portfolio/projeto_confirm_delete.html', {'projeto': projeto})

def projeto_detail_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    return render(request, 'portfolio/projeto_detail.html', {
        'projeto': projeto
    })

def licenciatura_detail_view(request, lic_id):
    lic = get_object_or_404(Licenciatura, id=lic_id)

    return render(request, 'portfolio/licenciatura_detail.html', {
        'lic': lic
    })


def licenciatura_create(request):
    if request.method == 'POST':
        form = LicenciaturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licenciaturas')
    else:
        form = LicenciaturaForm()

    return render(request, 'portfolio/licenciatura_form.html', {'form': form})


def licenciatura_update(request, pk):
    lic = get_object_or_404(Licenciatura, pk=pk)

    if request.method == 'POST':
        form = LicenciaturaForm(request.POST, request.FILES, instance=lic)
        if form.is_valid():
            form.save()
            return redirect('licenciaturas')
    else:
        form = LicenciaturaForm(instance=lic)

    return render(request, 'portfolio/licenciatura_form.html', {'form': form})


def licenciatura_delete(request, pk):
    lic = get_object_or_404(Licenciatura, pk=pk)

    if request.method == 'POST':
        lic.delete()
        return redirect('licenciaturas')

    return render(request, 'portfolio/licenciatura_confirm_delete.html', {'lic': lic})

def tecnologia_create(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()

    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Tecnologia'})


def tecnologia_update(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Tecnologia'})


def tecnologia_delete(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)

    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')

    return render(request, 'portfolio/confirm_delete_generico.html', {
        'objeto': tecnologia,
        'voltar_url': 'tecnologias',
        'titulo': 'Tecnologia'
    })


def competencia_create(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()

    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Competência'})


def competencia_update(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)

    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)

    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Competência'})


def competencia_delete(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)

    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')

    return render(request, 'portfolio/confirm_delete_generico.html', {
        'objeto': competencia,
        'voltar_url': 'competencias',
        'titulo': 'Competência'
    })


def formacao_create(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()

    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Formação'})


def formacao_update(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)

    if request.method == 'POST':
        form = FormacaoForm(request.POST, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'portfolio/form_generico.html', {'form': form, 'titulo': 'Formação'})


def formacao_delete(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)

    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')

    return render(request, 'portfolio/confirm_delete_generico.html', {
        'objeto': formacao,
        'voltar_url': 'formacoes',
        'titulo': 'Formação'
    })

from .models import Docente
def docente_detail_view(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)

    return render(request, 'portfolio/docente_detail.html', {
        'docente': docente
    })

def sobre_view(request):
    tecnologias = Tecnologia.objects.all().order_by('categoria')
    return render(request, 'portfolio/sobre.html', {'tecnologias': tecnologias})