from django.contrib import admin

from .models import (
    Licenciatura, Docente, UnidadeCurricular,
    Tecnologia, Projeto, TFC,
    Competencia, Formacao, MakingOf
)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "instituicao", "ano_inicio", "ano_fim")
    search_fields = ("nome", "sigla", "instituicao")


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "url_pagina_lusofona", "linkedin")
    search_fields = ("nome", "email")


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "licenciatura", "ano_curricular", "semestre", "ects")
    search_fields = ("nome", "sigla")
    list_filter = ("licenciatura", "ano_curricular", "semestre")
    filter_horizontal = ("docentes",)
    autocomplete_fields = ("licenciatura",)


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "url", "interesse")  # atualizado
    search_fields = ("nome", "categoria")
    list_filter = ("categoria", "interesse")  # atualizado


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "uc", "data_inicio", "data_fim", "url_github", "video")  # atualizado
    search_fields = ("titulo", "descricao", "conceitos_aplicados")
    list_filter = ("uc__licenciatura",)
    filter_horizontal = ("tecnologias",)
    autocomplete_fields = ("uc",)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "licenciatura", "classificacao")  # atualizado
    search_fields = ("titulo", "autor")
    list_filter = ("ano", "licenciatura", "classificacao")  # atualizado
    autocomplete_fields = ("licenciatura",)


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
    list_display = ("entidade", "titulo", "data")
    search_fields = ("titulo", "descricao_decisoes", "erros_encontrados")
    list_filter = ("entidade", "data")