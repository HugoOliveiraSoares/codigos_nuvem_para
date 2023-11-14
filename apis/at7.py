import sqlite3
import requests
from datetime import date


url = 'https://api.hgbrasil.com/finance?fields=only_results,EUR,USD&key=55068698'


conn = sqlite3.connect('bdcotacoes.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS moedas (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   data INTEGER,
                   dolar INTEGER,
                   euro INTEGER
                   )
               """)


r = requests.get(url)
if (r.status_code == 200):
    print("REQUISIÇÃO COM SUCESSO")
    json = r.json()
    today = date.today()
    cursor.execute(f"""
               INSERT INTO moedas
               (id, "data", dolar, euro)
               VALUES(1, {today}, {json['currencies']['USD']['buy']}, {json['currencies']['EUR']['buy']});
               """)
    conn.commit()
    print("INSERT COM SUCESSO")
else:
    print('Nao houve sucesso na requisicao.')


conn.close()
