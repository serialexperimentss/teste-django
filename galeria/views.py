# galeria/views.py
#from django.shortcuts import render

#def index(request):
#    return render(request, 'galeria/index.html')

#def imagem(request):
#    return render(request, 'galeria/imagem.html')
# galeria/views.py
from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects
        .order_by("data_fotografia")
        .filter(publicada=True)
    return render(
        request, 
        'galeria/index.html', 
        {"cards": fotografias}
    )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(
        request, 
        'galeria/imagem.html', 
        {"fotografia": fotografia}
    )