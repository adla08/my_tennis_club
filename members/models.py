from django.db import models


class Conteudo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    conteudo_html = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Menu(models.Model):
    TIPO_INTERNO = 'interno'
    TIPO_EXTERNO = 'externo'

    TIPOS_DESTINO = [
        (TIPO_INTERNO, 'Conteúdo interno'),
        (TIPO_EXTERNO, 'Link externo'),
    ]

    titulo = models.CharField(max_length=100)
    tipo_destino = models.CharField(
        max_length=20,
        choices=TIPOS_DESTINO
    )
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    url_externa = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo
