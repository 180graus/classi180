# -*- coding:utf-8 -*-
from django import forms
from django.contrib.localflavor.br.br_states import STATE_CHOICES

#from subscription.models import Subscription

#class SubscriptionForm(forms.ModelForm): class Meta:
#model = Subscription exclude = ('created_at',)
#fs = FileSystemStorage(location='/Users/Wouker/Projetos/proj_classi180/classificados/media/')

class FormContato(forms.Form):
    #nome = forms.CharField()
    #email = forms.EmailField(label=u'E-mail')
    #estado = forms.ChoiceField(choices=STATE_CHOICES)
	#cidade = forms.CharField()
    #mensagem = forms.CharField(widget=forms.Textarea())
    acao = models.CharField(max_length=1)
    #categoria = forms.CharField(Categoria)
    #subcategoria = forms.CharField(Subcategoria)
    #anunciante = forms.CharField(Anunciante)
    titulo = models.CharField(max_length = 70)
    #descricao = forms.TextField(max_length = 400)
    tag = models.CharField(max_length = 25)
    preco = models.CharField(max_length = 15)
	#photo = forms.FileField(required=False) 
	
def clean_nome(self):
        if self.cleaned_data['nome']=='Teste':
            raise forms.ValidationError(u'Digite um nome melhor.')
        else:
            return self.cleaned_data['nome']
