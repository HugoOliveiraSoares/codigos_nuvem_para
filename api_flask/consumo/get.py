import requests

r = requests.get("http://localhost:5000/api-loja/produtos/")

print(r.json())
