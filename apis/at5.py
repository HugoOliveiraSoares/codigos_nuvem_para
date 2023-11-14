import requests
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

if (r.status_code == 200):
    print()
    print('Retorno : ', r.text)
    arquivo = open("resposta.txt", "x")
    arquivo.write(r.text)
    arquivo.close()
    print()
else:
    print('Nao houve sucesso na requisicao.')
