from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    instituicao = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    ano_inicio = models.IntegerField()
    ano_fim = models.IntegerField(null=True, blank=True)
    url_curso = models.URLField(blank=True)

    def __str__(self):
        return f"{self.sigla} – {self.nome}"

    class Meta:
        verbose_name_plural = "Licenciaturas"


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url_pagina_lusofona = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    foto = models.ImageField(upload_to="docentes/", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Docentes"
        ordering = ["nome"]


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20, blank=True)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    apresentacao = models.TextField(blank=True)
    codigo_curso = models.IntegerField(null=True, blank=True)
    codigo_uc = models.IntegerField(null=True, blank=True)

    licenciatura = models.ForeignKey(
        Licenciatura, on_delete=models.CASCADE, related_name="ucs"
    )

    docentes = models.ManyToManyField(
        Docente, blank=True, related_name="ucs"
    )

    # Novos atributos (vindos da API) - ex 5
    objetivos = models.TextField(blank=True)
    programa = models.TextField(blank=True)
    metodologia = models.TextField(blank=True)
    bibliografia = models.TextField(blank=True)
    natureza = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.sigla} – {self.nome}"

    class Meta:
        verbose_name_plural = "Unidades Curriculares"


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="tecnologias/", blank=True, null=True)
    url = models.URLField(blank=True)
    interesse = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Tecnologias"


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField(blank=True)
    url_github = models.URLField(blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to="projetos/", blank=True, null=True)
    video = models.URLField(blank=True)

    uc = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name="projetos"
    )

    tecnologias = models.ManyToManyField(
        Tecnologia, blank=True, related_name="projetos"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Projetos"


class TFC(models.Model):
    CLASSIFICACAO_CHOICES = [
        (1, "Sem Interesse"),
        (2, "Pouco Interessante"),
        (3, "Interessante"),
        (4, "Muito Interessante"),
        (5, "Perfeito"),
    ]

    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=200, blank=True)
    curso = models.CharField(max_length=200, blank=True)
    resumo = models.TextField(blank=True)
    rating = models.IntegerField(choices=CLASSIFICACAO_CHOICES, null=True, blank=True)
    orientador = models.ManyToManyField(Docente, blank=True)
    email = models.EmailField(blank=True)
    palavras_chave = models.CharField(max_length=300, blank=True, null=True)
    areas = models.CharField(max_length=300, blank=True, null=True)
    imagem = models.ImageField(upload_to="tfcs/", blank=True, null=True)

    tecnologias = models.ManyToManyField(
        Tecnologia, blank=True, related_name="tfcs"
    )

    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name="tfcs"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "TFCs"


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField()
    descricao = models.TextField(blank=True)

    tecnologias = models.ManyToManyField(
        Tecnologia, blank=True, related_name="competencias"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Competências"


class Formacao(models.Model):
    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    certificado = models.FileField(upload_to="certificados/", blank=True, null=True)

    tecnologias = models.ManyToManyField(
        Tecnologia, blank=True, related_name="formacoes"
    )

    def __str__(self):
        return f"{self.titulo} – {self.instituicao}"

    class Meta:
        verbose_name_plural = "Formações"


class MakingOf(models.Model):
    ENTIDADE_CHOICES = [
        ("licenciatura", "Licenciatura"),
        ("uc", "Unidade Curricular"),
        ("docente", "Docente"),
        ("projeto", "Projeto"),
        ("tecnologia", "Tecnologia"),
        ("tfc", "TFC"),
        ("competencia", "Competência"),
        ("formacao", "Formação"),
    ]

    entidade = models.CharField(max_length=30, choices=ENTIDADE_CHOICES)
    titulo = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    descricao_decisoes = models.TextField()
    erros_encontrados = models.TextField(blank=True)
    correcoes = models.TextField(blank=True)
    foto = models.ImageField(upload_to="makingof/", blank=True, null=True)

    def __str__(self):
        return f"[{self.get_entidade_display()}] {self.titulo}"

    class Meta:
        verbose_name = "Making Of"
        verbose_name_plural = "Making Of"
        ordering = ["-data"]