import requests

url = 'https://viacep.com.br/ws/'
endereco = 'MG/Belo Horizonte/Rua dos Aimores'
formato = '/json/'
r = requests.get(url + endereco + formato)

if (r.status_code == 200):
    print()
    for re in r.json():
        print('JSON : ', re)
        print()
else:
    print('Nao houve sucesso na requisicao.')

