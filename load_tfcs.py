import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import json
from django.conf import settings
from portfolio.models import TFC

path = os.path.join(settings.BASE_DIR, 'data', 'tfcs_2025.json')

with open(path, encoding='utf-8') as f:
    dados = json.load(f)

for item in dados:
    TFC.objects.create(
        titulo=item.get('titulo'),
        autor=item.get('autor'),
        ano=item.get('ano'),
        descricao=item.get('descricao', ''),
    )

print('Dados carregados com sucesso!')