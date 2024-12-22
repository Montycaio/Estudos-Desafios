import requests
import json

def api(filme):

    req = None
    #filme = 'avengers'

    try:
        #key = 'd7401903'

        req = requests.get(f'http://www.omdbapi.com/?t={filme}' + '&type=movie')

        dicionario = json.loads(req.text)
        return dicionario




    except:
        print('Erro na conexao')
        return None

a = input('Digite o nome do filme ou SAIR: ')

if a == 'sair':
    print('Saindo...')
    exit()
else:
    filme = api(a)
    print('Filme', filme['Title'])