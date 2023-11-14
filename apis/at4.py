import requests

url = 'https://viacep.com.br/ws/abc'
formato = '/json/'
r = requests.get(url + formato)

print(r.status_code)
print(r.reason)

