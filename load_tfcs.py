import json
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from portfolio.models import TFC

class Command(BaseCommand):
    help = 'Carrega TFCs do JSON'

    def handle(self, *args, **kwargs):
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

        self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso!'))