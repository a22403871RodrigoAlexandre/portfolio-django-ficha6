from django.contrib import admin

from .models import (
    Licenciatura, Docente, UnidadeCurricular,
    Tecnologia, Projeto, TFC,
    Competencia, Formacao, MakingOf
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nome", "instituicao", "ano_inicio", "ano_fim")
    search_fields = ("nome", "sigla", "instituicao")


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "url_pagina_lusofona", "linkedin")
    search_fields = ("nome", "email")


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nome", "ano_curricular", "semestre", "ects", "licenciatura")
    search_fields = ("nome", "sigla")
    list_filter = ("ano_curricular", "semestre", "licenciatura")
    filter_horizontal = ("docentes",)


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria")
    search_fields = ("nome",)
    list_filter = ("categoria",)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "uc", "data_inicio", "data_fim", "url_github")
    search_fields = ("titulo", "descricao", "conceitos_aplicados")
    list_filter = ("uc",)
    filter_horizontal = ("tecnologias",)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "licenciatura")
    search_fields = ("titulo", "autor", "resumo")
    list_filter = ("ano",)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel")
    search_fields = ("nome", "descricao")
    list_filter = ("tipo", "nivel")
    filter_horizontal = ("tecnologias",)


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "instituicao", "tipo", "data_inicio", "data_fim")
    search_fields = ("titulo", "instituicao")
    list_filter = ("tipo",)
    filter_horizontal = ("tecnologias",)


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo", "entidade", "data")
    search_fields = ("titulo", "descricao_decisoes", "erros_encontrados")
    list_filter = ("entidade", "data")