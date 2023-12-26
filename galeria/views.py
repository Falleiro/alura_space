from django.shortcuts import render


def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webtelescope.org / NASA/ James Webb"},
        2: {"nome": "Gláxia NGC 1079",
            "legenda": "webtelescope.org / NASA/ Hublle"}
    }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')



