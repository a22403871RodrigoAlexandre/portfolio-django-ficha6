from django.shortcuts import render, get_object_or_404
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Formacao
from .forms import ProjetoForm
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