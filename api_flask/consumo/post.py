import requests

data = { 'descricao':'TEST', 'ganhopercentual':'1' }

r = requests.post("http://localhost:5000/api-loja/produtos", json = data)

print(r.text)
