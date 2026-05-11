import os
from django.core.files import File
from portfolio.models import Docente, Tecnologia, Projeto, TFC, MakingOf

MEDIA_ROOT = '/Users/rodrigoalexandre/Documents/portfolio-django-ficha6/media'

# Docente
for obj in Docente.objects.all():
    if obj.foto and obj.foto.name:
        local_path = os.path.join(MEDIA_ROOT, obj.foto.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Docente: {obj}")

# Tecnologia
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join(MEDIA_ROOT, obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Tecnologia: {obj}")

# Projeto
for obj in Projeto.objects.all():
    if obj.foto and obj.foto.name:
        local_path = os.path.join(MEDIA_ROOT, obj.foto.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Projeto: {obj}")

# TFC
for obj in TFC.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(MEDIA_ROOT, obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado TFC: {obj}")

# MakingOf
for obj in MakingOf.objects.all():
    if obj.foto and obj.foto.name:
        local_path = os.path.join(MEDIA_ROOT, obj.foto.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado MakingOf: {obj}")