from django.contrib.syndication.feeds import Feed

from models import Anuncio

class UltimosAnuncios(Feed):
    title = 'Ultimos artigos do Classi180'
    link = '/'

    def items(self):
        return Anuncio.objects.all()

    def item_link(self, anuncio):
        return '/anuncio/%d/'%anuncio.id

  
