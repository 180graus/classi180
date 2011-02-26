# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/Users/Wouker/Projetos/proj_classi180/classificados/media/')

ACAO_CHOICES = (
               ('1', 'Comprar'),
               ('2', 'Vender'),
               )

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()
    

class Categoria(models.Model):

    nome = models.CharField(max_length=80)
    dt_cadastro = models.DateTimeField('Data de Cadastro')
    status = models.BooleanField(default=1, blank=False)

    def __unicode__(self):
        return self.nome

class Subcategoria(models.Model):

    nome = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria)
    dt_cadastro = models.DateTimeField('Data de Cadastro')
    status = models.BooleanField(default=1, blank=False)

    def __unicode__(self):
        return self.nome

class Estado(models.Model):

    REGIAO_CHOICES = (
        ('1', 'Norte'),
        ('2', 'Nordeste'),
        ('3', 'Centro-Oeste'),
        ('4', 'Sudeste'),
        ('5', 'Sul'),
    )

    nome = models.CharField(max_length=80)
    sigla = models.CharField(max_length=2)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)

    def __unicode__(self):
        return self.nome

class Cidade(models.Model):

    cidade = models.CharField(max_length=80)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return self.cidade
    
class Anunciante(models.Model):

    nome_completo = models.CharField(max_length = 60)
    nickname = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 75)
    endereco = models.CharField(max_length = 255)
    cidade = models.ForeignKey(Cidade)
    cep = models.CharField(max_length = 9)
    telefone = models.CharField(max_length = 35)
    dt_cadastro = models.DateTimeField('Data de Cadastro')
    status = models.BooleanField(default=1, blank=False)

    def __unicode__(self):
        return self.nome_completo

    def foi_publicado_hoje(self):
        return self.dt_cadastro.date() == datetime.date.today()

#class Secao(models.Model):

    #menu = models.CharField(max_length = 1, choices = MENU_CHIOCES)
    #aparencia = models.CharField(max_length = 2, choices = APARENCIAS_CHOICES)
    #parceiro = models.ForeignKey(Parceiro)
    #nome = models.CharField(max_length = 50)
    #url = models.URLField(verify_exists=True, max_length=200)
    #url = models.CharField(max_length=75)
    #status = models.BooleanField(default=1, blank=False)

    #class Meta:
        #db_table='classificados_secao'
        #verbose_name = u'Seção'
        #verbose_name_plural = u'Seções'

    #def __unicode__(self):
        #return self.nome

################################################################################

class Anuncio(models.Model):

    class Meta:
        ordering = ('-dt_cadastro',)

    #secao = models.ForeignKey(Secao)
    acao = models.CharField(max_length=1, choices=ACAO_CHOICES)
    categoria = models.ForeignKey(Categoria)
    subcategoria = models.ForeignKey(Subcategoria)
    anunciante = models.ForeignKey(Anunciante)
    titulo = models.CharField(max_length = 70)
    descricao = models.TextField(max_length = 400)
    tag = models.CharField(max_length = 25)
    preco = models.CharField(max_length = 15)
    dt_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    dt_saida = models.DateTimeField('Data de Saída', null=True, blank=False)    
    #tipoanuncio = models.CharField(max_length=1, choices=AnuncioType_CHOICES)
    photo = models.FileField(upload_to='/Users/Wouker/Projetos/proj_classi180/classificados/media/', null=True, blank=True)   
    status = models.BooleanField(default=1, blank=False)
    def get_absolute_url(self): 
        return str(MEDIA_URL + self.arquivo).replace("\\", "/") 

    def get_absolute_url(self):
        return '/anuncio/%d/'%self.id
	#def get_field_url(self): 
     #   return (MEDIA_URL + self.arquivo).replace("\\", "/") 

    def __unicode__(self):
        return self.titulo
