# Manchetes BBC
import requests
from bs4 import BeautifulSoup

manchetes = []
n = 0
sites = []
pType = [] # To parser/scrap the page
pClass = [] # To parser/scrap the page

while True: # Emulate Do while
  print("Choose\n-> ", end='')
  opt = input()
  if(opt.lower()=="help"): # Compara com os caracteres em casa baixa
    print(f'{"_" * 110} \n')
    print(f'\033[32m\n{" Help ":^110}\033[m')
    print(f'{"_" * 110} \n')
    print("Type:\n-> 'br' to only pt-br news\n-> 'us' to only en-us news\n-> 'tech' to only tech news\n-> '$' to economy news\n-> 'clear' or 'cls' to 'clean' the screen\nWarnings:\n - example: ('br-tech' to only pt-br tech news or 'us-tech' to only en-us tech news")
    print(f'{"_" * 110} \n')
  if(opt.lower()=='cls' or opt.lower()=='clear'):
    print(f'{" " * 112345}')
  if(opt.lower()=='br'):
    n = n+1
    sites = ['https://www.bbc.com/portuguese', 'https://g1.globo.com/']
    pType = ['span', 'a']
    pClass = ['title-link__title-text', 'feed-post-link']
    break;

print(f'{"_" * 110} \n')
for i in range(0, n+1):
  request = requests.get(sites[i])
  soup = BeautifulSoup(request.text, 'html.parser')
  info = soup.find_all(pType[i], class_=pClass[i])

  for texto in info:
    manchetes.append(texto.get_text().split('\n'))
  nome = sites[i]
  nome = nome.replace('.com', ' ')
  nome = nome.replace('https://', '')
  nome = nome.replace('http://.', '')
  nome = nome.replace('www.', '')
  nome = nome.replace('/', '')
  nome = ("Manchetes: "+nome)
  print(f'\033[31m\n{nome.upper():^110}\033[m')
  print(f'{"_" * 110} \n')

  for manchete in manchetes:
    aux = manchete
    print("->",aux[0])

  manchetes.clear()
  print(f'{"_" * 110} \n')