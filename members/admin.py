from django.contrib import admin
from .models import Conteudo, Menu


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "slug", "ativo")
    prepopulated_fields = {"slug": ("titulo",)}
    list_filter = ("ativo",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo_destino", "ordem", "ativo")
    list_filter = ("tipo_destino", "ativo")
    ordering = ("ordem",)

