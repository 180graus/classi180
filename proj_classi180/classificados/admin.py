from django.contrib import admin
from models import Artigo
from models import Categoria
from models import Subcategoria
from models import Estado,Cidade
from models import Anuncio
from models import Anunciante
#from models import Secao

class AnuncioAdmin(admin.ModelAdmin):
        prepopulated_fields = {'preco': ('titulo','tag')}
	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Artigo)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Anuncio,AnuncioAdmin)
admin.site.register(Anunciante)
#admin.site.register(Secao)
