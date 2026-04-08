import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.conf import settings
from portfolio.models import TFC, Licenciatura

path = os.path.join(settings.BASE_DIR, 'data', 'tfcs_2025.json')

if not os.path.exists(path):
    print("Ficheiro JSON não encontrado!")
    exit()

with open(path, encoding='utf-8') as f:
    dados = json.load(f)

# 🎓 Garantir que existe uma licenciatura
licenciatura, _ = Licenciatura.objects.get_or_create(
    nome="Engenharia Informática",
    defaults={
        "sigla": "EI",
        "instituicao": "Universidade Lusófona",
        "ano_inicio": 2022
    }
)

count = 0
erros = 0

for item in dados:
    try:
        titulo = item.get('titulo')

        
        if not titulo:
            erros += 1
            print("⚠️ TFC ignorado (sem título)")
            continue

        tfc, created = TFC.objects.get_or_create(
            titulo=titulo,
            defaults={
                'autor': item.get('autor', ''),
                'curso': item.get('curso', ''),
                'resumo': item.get('resumo', ''),
                'rating': item.get('rating'),
                'orientador': item.get('orientador', ''),
                'email': item.get('email', ''),
                'palavras_chave': item.get('palavras_chave', ''),
                'areas': item.get('areas', ''),
                'licenciatura': licenciatura
            }
        )

        if created:
            count += 1
            print(f"✔ Criado: {titulo}")
        else:
            print(f"⚠ Já existe: {titulo}")

    except Exception as e:
        erros += 1
        print(f"❌ Erro ao processar '{item}': {e}")

print("\n📊 RESUMO:")
print(f"✔ Novos TFCs: {count}")
print(f"⚠ Ignorados/Erros: {erros}")