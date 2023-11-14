import requests
# 55068698

url = 'https://api.hgbrasil.com/finance?fields=only_results,EUR,USD&key=55068698'
r = requests.get(url)

if (r.status_code == 200):
    json = r.json()
    print(json['currencies']['USD']['buy'])
else:
    print('Nao houve sucesso na requisicao.')

