from django.contrib import admin
from .models import Artigo, Like, Comentario


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_criacao', 'total_likes', 'total_comentarios']
    list_filter = ['autor', 'data_criacao']
    search_fields = ['titulo', 'texto']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'artigo', 'data_criacao']
    list_filter = ['autor', 'artigo']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['artigo', 'user', 'session_key', 'created_at']
