from django.conf.urls.defaults import *
from proj_classi180.classificados import views
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from classificados.models import Anuncio

from classificados.feeds import UltimosAnuncios

#Categorias, Cidades, Estados, Subcategorias
#from classificados.models import Categorias
urlpatterns = patterns('',
    # Example:
    # (r'^proj_classi180/', include('proj_classi180.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.generic.date_based.archive_index',
     {'queryset': Anuncio.objects.all(), 'date_field': 'dt_cadastro'}),# retorna o anuncio de acordo com a data
    (r'^admin/(.*)', admin.site.root),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',# retorna as feeds com url
        {'feed_dict': {'ultimos': UltimosAnuncios}}),
    (r'^anuncio/(?P<anuncio_id>\d+)/$', 'classificados.views.anuncio'),
	(r'^down/(?P<path>.*)$','django.views.static.serve',
	{'document_root': '/Users/Wouker/Projetos/proj_classi180/classificados/media/', 'show_indexes':False}), 
    (r'^contato/$', 'views.contato'),
	(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),
	
	#(r'^contato/listar$','proj_classi180.classificados.views.contato')
	(r'^contato/criar$','django.views.generic.create_update.create_object',
		{'model':Anuncio,'template_name':'generic_form.html','post_save_redirect' : ''}),
		
		    #urlpatterns = patterns('classificados.views',
        #url(r'^$', 'subscribe', name='subscribe'),
        #route(r'^(\d+)/sucesso/$', GET='new', POST='create', name='success'),
    
)
