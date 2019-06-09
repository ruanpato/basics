# Projeto notícias vai utilizar o código manchetes como esboço para permitir ver notícias via terminal
sites=[]

class Noticia(object):
    id = 0 # Inicia o id da classe Noticia, para a escolha do usuário
    def __init__(self, manchete, texto, mendereco): # Método construtor
        self.manchete = manchete
        self.texto = texto
        self.mendereco = mendereco # Endereço da matéria
        self.id = Noticia.id # Atribui o id para o objeto criado
        Noticia.id += 1 # Incrementa o id

class Site(object): # Classe para os sites de notícia
    id = 0 # Inicia o id da classe Site.
    def __init__(self, nome, endereco, mclasse, mtag, tclasse, ttag):
        self.nome = nome
        self.endereco = endereco # Endereco do site
        self.mclasse = mclasse # Classe HTML onde a manchete se encontra
        self.mtag = mtag # Tag HTML onde se encontra a manchete
        self.tclasse = tclasse # Classe HTML onde o texto se encontra
        self.id = Site.id # Atribui um id para o site
    

''' 
Função provisória para criar os objetos dos sites de notícias, pois os sites se distinguem (HTML).
'''
def provisorio():
    sites.append(Site('BBC Português', 'https://www.bbc.com/portuguese', 'title-link__title-text', 'span', ' ', ' '))
    sites.append(Site('G1 Noticias', 'https://www.bbc.com/portuguese', 'title-link__title-text', 'span', ' ', ' '))