from django.db import models
from django.contrib.auth.models import User


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.likes.count()

    def total_comentarios(self):
        return self.comentarios.count()


class Like(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        who = self.user.username if self.user else f'anon({self.session_key[:8]})'
        return f'{who} → {self.artigo.titulo}'


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_criacao']

    def __str__(self):
        return f'{self.autor.username} em "{self.artigo.titulo}"'
