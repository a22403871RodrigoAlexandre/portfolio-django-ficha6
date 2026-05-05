from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm, ComentarioForm


def _is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def artigos_list(request):
    artigos = Artigo.objects.select_related('autor').all()
    return render(request, 'artigos/artigos_list.html', {'artigos': artigos})


def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.select_related('autor').all()
    form = ComentarioForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'/accounts/login/?next=/artigos/{pk}/')
        form = ComentarioForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.artigo = artigo
            c.autor = request.user
            c.save()
            return redirect('artigo_detail', pk=pk)

    # Verifica se o utilizador atual já deu like
    user_liked = False
    if request.user.is_authenticated:
        user_liked = artigo.likes.filter(user=request.user).exists()
    elif request.session.session_key:
        user_liked = artigo.likes.filter(session_key=request.session.session_key, user=None).exists()

    return render(request, 'artigos/artigo_detail.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form,
        'user_liked': user_liked,
        'total_likes': artigo.total_likes(),
        'pode_editar': request.user == artigo.autor and _is_autor(request.user),
    })


def artigo_like(request, pk):
    if request.method != 'POST':
        return redirect('artigo_detail', pk=pk)

    artigo = get_object_or_404(Artigo, pk=pk)

    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(artigo=artigo, user=request.user)
        if not created:
            like.delete()
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        like, created = Like.objects.get_or_create(artigo=artigo, session_key=session_key, user=None)
        if not created:
            like.delete()

    return redirect('artigo_detail', pk=pk)


@login_required
def artigo_create(request):
    if not _is_autor(request.user):
        messages.error(request, 'Não tens permissão para criar artigos.')
        return redirect('artigos_list')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigo_detail', pk=artigo.pk)
    else:
        form = ArtigoForm()

    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Novo Artigo'})


@login_required
def artigo_update(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if not _is_autor(request.user) or artigo.autor != request.user:
        messages.error(request, 'Só podes editar os teus próprios artigos.')
        return redirect('artigo_detail', pk=pk)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigo_detail', pk=pk)
    else:
        form = ArtigoForm(instance=artigo)

    return render(request, 'artigos/artigo_form.html', {'form': form, 'titulo': 'Editar Artigo', 'artigo': artigo})


@login_required
def artigo_delete(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)

    if not _is_autor(request.user) or artigo.autor != request.user:
        messages.error(request, 'Só podes apagar os teus próprios artigos.')
        return redirect('artigo_detail', pk=pk)

    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos_list')

    return render(request, 'artigos/artigo_confirm_delete.html', {'artigo': artigo})
