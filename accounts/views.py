from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings as django_settings
from .forms import RegisterForm, MagicLinkRequestForm
from .models import MagicLinkToken


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            autores_group, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(autores_group)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '/')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            messages.error(request, 'Username ou password incorretos.')
    return render(request, 'accounts/login.html', {
        'magic_link_form': MagicLinkRequestForm(),
        'next': next_url,
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def magic_link_request(request):
    if request.method == 'POST':
        form = MagicLinkRequestForm(request.POST)
        if form.is_valid():
            email_addr = form.cleaned_data['email']
            token_obj = MagicLinkToken.objects.create(email=email_addr)
            link = request.build_absolute_uri(f'/accounts/magic-link/verify/{token_obj.token}/')

            if django_settings.DEBUG:
                # Em desenvolvimento: imprime o URL directamente no terminal
                # (evita o QP encoding do MIME que parte URLs longas em múltiplas linhas)
                import sys
                print(f'\n{"=" * 60}\nMAGIC LINK:\n{link}\n{"=" * 60}\n', flush=True, file=sys.stderr)
                messages.success(request, 'Link gerado! Copia o URL da consola do servidor.')
            else:
                msg = EmailMessage(
                    subject='O teu link de acesso ao Portfolio',
                    body=f'Clica neste link para entrar:\n\n{link}\n\nExpira em 15 minutos.',
                    from_email=django_settings.DEFAULT_FROM_EMAIL,
                    to=[email_addr],
                )
                msg.send()
                messages.success(request, 'Link enviado! Verifica o teu email.')
    return redirect('login')


def magic_link_verify(request, token):
    try:
        magic = MagicLinkToken.objects.get(token=token)
    except MagicLinkToken.DoesNotExist:
        messages.error(request, 'Link inválido.')
        return redirect('login')

    if not magic.is_valid():
        messages.error(request, 'Link expirado ou já utilizado.')
        return redirect('login')

    try:
        user = User.objects.get(email=magic.email)
    except User.DoesNotExist:
        messages.error(request, 'Nenhuma conta encontrada com este email.')
        return redirect('login')

    magic.used = True
    magic.save()
    login(request, user)
    return redirect('home')
