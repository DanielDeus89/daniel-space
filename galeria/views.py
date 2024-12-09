from django.shortcuts import get_object_or_404, render

from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicadas=True)
    return render(request, 'galeria/index.html', {'cards':fotografias})
    

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{'fotografia':fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicadas=True)
    
    if 'buscar' in request.GET:
        # nome_a_buscar = request.GET.get[('buscar', '').strip()]
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    
    return render(request, "galeria/buscar.html", {'cards':fotografias})
