import requests

ceps = [30140071, 30140072, 30140073, 30140074, 30140075]

url = 'https://viacep.com.br/ws/'
formato = '/json/'

for cep in ceps:
    r = requests.get(url + str(cep) + formato)
    if (r.status_code == 200):
        print()
        print('JSON : ', r.json())
        print()
    else:
        print('Nao houve sucesso na requisicao.')
