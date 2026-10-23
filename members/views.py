from django.shortcuts import render, get_object_or_404
from .models import Conteudo, Menu


def home(request):
    menus = Menu.objects.filter(ativo=True).order_by('ordem')
    return render(request, 'home.html', {'menus': menus})


def conteudo(request, slug):
    menus = Menu.objects.filter(ativo=True).order_by('ordem')
    pagina = get_object_or_404(Conteudo, slug=slug, ativo=True)

    return render(request, 'conteudo.html', {
        'menus': menus,
        'pagina': pagina,
    })
