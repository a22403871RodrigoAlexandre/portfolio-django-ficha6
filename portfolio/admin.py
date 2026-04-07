from django.contrib import admin

from .models import (
    Licenciatura, Docente, UnidadeCurricular,
    Tecnologia, Projeto, TFC,
    Competencia, Formacao, MakingOf
)

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nome", "instituicao", "ano_inicio", "ano_fim", "grau")
    search_fields = ("nome", "sigla", "instituicao")
    list_filter = ("grau", "instituicao")

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "url_pagina_lusofona")
    search_fields = ("nome", "email")

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nome", "ano_curricular", "semestre", "ects", "licenciatura")
    search_fields = ("nome", "sigla")
    list_filter = ("ano_curricular", "semestre", "licenciatura")
    filter_horizontal = ("docentes",)  # widget mais cómodo para ManyToMany


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "nivel_interesse")
    search_fields = ("nome",)
    list_filter = ("categoria", "nivel_interesse")

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "uc", "data_inicio", "data_fim", "url_github")
    search_fields = ("titulo", "descricao", "conceitos_aplicados")
    list_filter = ("uc", "tecnologias")
    filter_horizontal = ("tecnologias",)



@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "interesse")
    search_fields = ("titulo", "autor", "resumo")
    list_filter = ("ano", "interesse")
    filter_horizontal = ("tecnologias",)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel")
    search_fields = ("nome", "descricao")
    list_filter = ("tipo", "nivel")
    filter_horizontal = ("tecnologias", "projetos")


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "instituicao", "tipo", "data_inicio", "data_conclusao")
    search_fields = ("titulo", "instituicao")
    list_filter = ("tipo",)
    filter_horizontal = ("tecnologias",)



@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo", "entidade", "data")
    search_fields = ("titulo", "descricao_decisoes", "erros_encontrados")
    list_filter = ("entidade", "data")