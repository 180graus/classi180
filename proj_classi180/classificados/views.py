from classificados.models import Anuncio
from django.core.context_processors import request #feito de depois
from django.shortcuts import render_to_response

#def anuncio(request, anuncio_id):
    #return render_to_response('classificados/anuncio.html')

#from models import Anuncio

def anuncio(request, anuncio_id):
    anuncio = Anuncio.objects.get(id=anuncio_id)
    return render_to_response('classificados/anuncio.html', locals())

