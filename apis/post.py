import json
import requests

dado = {'matricula' : 'E01381'}

url = 'http://localhost:8080/alunos'

r = requests.post(url, json=dado)
