from classificados.models import Anuncio
from django.core.context_processors import request
from django.shortcuts import render_to_response

from django.template import RequestContext

def contato(request):
	contatos = Anuncio.objects.all()
	return render_to_response('list.html',{'contatos':contatos})
    #return render_to_response('list.html',locals(),context_instance=RequestContext(request),)
	
#################################################################################
#arquivo que salva no banco
